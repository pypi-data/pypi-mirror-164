# -*- coding: utf-8 -*-
# 2018 to present - Copyright Microchip Technology Inc. and its subsidiaries.

# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.

# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL,
# PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY
# KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP
# HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

import os
import shutil
import cryptoauthlib as cal
from intelhex import IntelHex
import cryptography
from cryptography.hazmat.primitives import hashes

from tpds.resource_generation import ResourceGeneration
from tpds.flash_program import FlashProgram
from tpds.secure_element import ECC608A
from tpds.tp_utils.tp_settings import TPSettings
import tpds.tp_utils.tp_input_dialog as tp_userinput
from tpds.tp_utils.tp_print import print
from tpds.tp_utils.tp_keys import TPAsymmetricKey, TPSymmetricKey
from tpds.tp_utils.tp_utils import sign_on_host
from tpds.tp_utils.tp_utils import pretty_print_hex


class FirmwareValidationUsecase():
    def __init__(self, boards, secboot_pubkey_slot=15,
                 io_protection_key_slot=6,
                 boot_start_addr=0x00000000,
                 boot_end_addr=0x0000BFFF,
                 app_start_addr=0x0000C000,
                 app_end_addr=0x0003FBFF,
                 sign_start_addr=0x0003FC00,
                 app_len_str_addr=0x0003FD00):
        self.boards = boards
        self.io_protection_key_slot = io_protection_key_slot
        self.secboot_pubkey_slot = secboot_pubkey_slot
        self.boot_start_addr = boot_start_addr
        self.boot_end_addr = boot_end_addr
        self.app_start_addr = app_start_addr
        self.app_end_addr = app_end_addr
        self.sign_start_addr = sign_start_addr
        self.app_len_str_addr = app_len_str_addr

    def generate_resources(self, b=None):
        self.__connect_to_SE(b)

        print('Generating crypto assets for Usecase...', canvas=b)
        privkey_file = self.__get_private_key_file(b)
        self.secbootkey = TPAsymmetricKey(privkey_file)
        self.secbootkey.get_private_pem(privkey_file)
        resources = ResourceGeneration()
        # secure boot public key
        assert resources.load_public_key(
                    self.secboot_pubkey_slot,
                    self.secbootkey.get_public_key_bytes()) \
               == cal.Status.ATCA_SUCCESS, \
               "Loading Secure Boot public key failed"

        # io protection key
        ip_key_file = 'slot_{}_secret_key'.format(
                                self.io_protection_key_slot) + '.pem'
        self.ip_key = TPSymmetricKey(ip_key_file)
        assert resources.load_secret_key(
                    self.io_protection_key_slot,
                    self.ip_key.get_bytes()) \
               == cal.Status.ATCA_SUCCESS, \
               "Loading io protection key failed"
        print('OK', canvas=b)

    def sign_firmware(self, b=None):
        self.__create_combined_firmware(b)

        print('Signing combined image firmware hex...', canvas=b)
        # load data from combined hex image
        addrs = self.combined.segments()
        (unused, end_addr) = addrs[len(addrs)-2]
        tbs = self.combined.tobinarray(start=0x00000000, size=end_addr)

        # calculate digest
        tbs_digest = hashes.Hash(
            hashes.SHA256(),
            backend=cryptography.hazmat.backends.default_backend()
        )
        tbs_digest.update(tbs)
        self.digest = tbs_digest.finalize()[:32]
        print('Combined hex digest:', canvas=b)
        print(pretty_print_hex(self.digest), canvas=b)

        # Sign the combined hex image
        self.signature = sign_on_host(
                        self.digest,
                        self.secbootkey.get_private_key())
        print('Signature:', canvas=b)
        print(pretty_print_hex(self.signature), canvas=b)

        # Add signature to combined hex image
        self.combined.puts(self.sign_start_addr, self.signature)
        app_len = end_addr - self.app_start_addr
        self.combined.puts(
                        self.app_len_str_addr,
                        app_len.to_bytes(4, 'little'))
        self.combined.tofile(self.combined_hex, format='hex')

        # Perform Secure boot update to SE slot
        self.verify_firm_and_update_digest(b)

    def compute_firmware_digest_and_get_sign(self, b=None):
        # Here We are just using digest calucalted on previous step
        # This digest computation will happen again on host MCU
        print('Digest:', canvas=b)
        print(pretty_print_hex(self.digest), canvas=b)

        print('Signature:', canvas=b)
        print(pretty_print_hex(self.signature), canvas=b)

    def verify_firm_and_update_digest(self, b=None):
        print("Updating new digest to SE slot...", canvas=b)
        host_random = os.urandom(32)
        is_verified = cal.AtcaReference(False)
        assert cal.atcab_secureboot_mac(
                    0x07,  # SECUREBOOT_MODE_FULL_COPY
                    self.digest,
                    self.signature,
                    host_random,
                    self.ip_key.get_bytes(),
                    is_verified) == cal.Status.ATCA_SUCCESS, \
               "Secure Boot command failed"

        assert is_verified.value, "Failed"
        print('Completed', canvas=b)

    def verify_firm_based_on_digest(self, b=None):
        print("Validating Firmware based on stored digest in SE...", canvas=b)
        host_random = os.urandom(32)
        is_verified = cal.AtcaReference(False)
        assert cal.atcab_secureboot_mac(
                    0x06,  # SECUREBOOT_MODE_FULL_STORE
                    self.digest,
                    self.signature,
                    host_random,
                    self.ip_key.get_bytes(),
                    is_verified) == cal.Status.ATCA_SUCCESS, \
               "Secureboot command failed"

        assert is_verified.value, "Falied"
        print('Completed', canvas=b)

    def flash_combined_firmware(self, b=None):
        flash_firmware = FlashProgram()
        print(f'Programming {self.combined_hex} file...', canvas=b)
        flash_firmware.check_board_status()
        flash_firmware.load_hex_image(self.combined_hex)
        print('Success', canvas=b)

    def __connect_to_SE(self, b=None):
        print('Connect to Secure Element: ', canvas=b)
        if self.boards is None:
            print('Prototyping board MUST be selected!', canvas=b)
            return
        assert self.boards.get_selected_board(), \
            'Select board to run an Usecase'

        kit_parser = FlashProgram()
        print(kit_parser.check_board_status())
        assert kit_parser.is_board_connected(), \
            'Check the Kit parser board connections'
        factory_hex = self.boards.get_kit_hex()
        if not kit_parser.is_factory_programmed():
            assert factory_hex, \
                'Factory hex is unavailable to program'
            print('Programming factory hex...', canvas=b)
            tp_settings = TPSettings()
            path = os.path.join(
                tp_settings.get_tpds_core_path(),
                'assets', 'Factory_Program.X',
                factory_hex)
            print(f'Programming {path} file')
            kit_parser.load_hex_image(path)
        element = ECC608A(address=0x6C)
        print('OK', canvas=b)
        print('Device details: {}'.format(element.get_device_details()))
        self.ser_num = element.get_device_serial_number().hex().upper()

    def __get_boot_hex_and_app_hex(self, b=None):
        print('Select Firmware Validation boot file...', canvas=b)
        boot = tp_userinput.TPInputFileUpload(
                                    file_filter=['*.hex'],
                                    nav_dir = os.getcwd(),
                                    dialog_title='Upload boot hex')
        boot.invoke_dialog()
        print(
            f'Selected Boot hex file is: {boot.file_selection}',
            canvas=b)
        assert boot.file_selection is not None, \
            'Select valid boot hex file'

        print('Select Application image file...', canvas=b)
        app = tp_userinput.TPInputFileUpload(
                                    file_filter=['*.hex'],
                                    nav_dir = os.getcwd(),
                                    dialog_title='Upload app hex')
        app.invoke_dialog()
        print(
            f'Selected Application file is: {app.file_selection}',
            canvas=b)
        assert app.file_selection is not None, \
            'Select valid Application image file'

        return {
            'boot': boot.file_selection,
            'app': app.file_selection
        }

    def __create_combined_firmware(self, b=None):
        hex_files = self.__get_boot_hex_and_app_hex(b)
        self.combined_hex = 'combined_image.hex'
        self.combined = IntelHex()

        print('Combining boot and application image...', canvas=b)
        boot_hex = 'boot.hex'
        shutil.copy(hex_files.get('boot'), boot_hex)
        self.combined.merge(IntelHex(boot_hex), overlap='replace')
        os.remove(boot_hex)

        app_hex = 'applicaion.hex'
        shutil.copy(hex_files.get('app'), app_hex)
        self.combined.merge(IntelHex(app_hex), overlap='replace')
        os.remove(app_hex)

        self.combined.tofile(self.combined_hex, format='hex')
        print('Completed', canvas=b)
        print(f'Combined image file is: {self.combined_hex}', canvas=b)

    def __get_private_key_file(self, b=None):
        print('Select Secure Boot private key option', canvas=b)
        item_list = ['Generate Private key', 'Upload Private key']
        dropdown_desc = (
        '''<font color=#0000ff><b>Select Secure Boot private key option</b>
        </font><br>
        <br>Generate Private key - Generates new Secure Boot private key<br>
        Upload Private key - Use existing private key file. Requires
        private key file .pem<br>''')
        user_input = tp_userinput.TPInputDropdown(
                                    item_list=item_list,
                                    desc=dropdown_desc,
                                    dialog_title='Private key Selection')
        user_input.invoke_dialog()
        print(f'Selected option is: {user_input.user_option}', canvas=b)
        assert user_input.user_option is not None, \
            'Select valid private key Option'

        if user_input.user_option == 'Upload Private key':
            print('Select private key file...', canvas=b)
            privkey = tp_userinput.TPInputFileUpload(
                                        file_filter=['*.pem'],
                                        nav_dir = os.getcwd(),
                                        dialog_title='Upload Private key')
            privkey.invoke_dialog()
            print(
                f'Selected private key file is: {privkey.file_selection}',
                canvas=b)
            assert privkey.file_selection is not None, \
                'Select valid private key file'
            return privkey.file_selection
        else:
            privkey_file = 'slot_{}_ecc_private_key'.format(
                                self.secboot_pubkey_slot) + '.pem'
            return privkey_file
