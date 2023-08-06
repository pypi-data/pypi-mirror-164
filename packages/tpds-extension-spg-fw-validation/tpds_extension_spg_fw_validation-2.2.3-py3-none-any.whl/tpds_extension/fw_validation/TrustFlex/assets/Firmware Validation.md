# Trust Platform Design Suite - Usecase Help - Firmware Validation

This document helps to understand Pre and Post steps of Usecase transaction diagram.

## Setup requirements
 - [DM320118](https://www.microchip.com/developmenttools/ProductDetails/DM320118)
 - [MPLAB X IDE](https://www.microchip.com/en-us/development-tools-tools-and-software/mplab-x-ide) 5.45 or above

## Pre Usecase transaction Steps
 - Connect DM320118 board to PC running Trust Platform Design Suite
 - Ensure *MPLAB X Path* is set in *File* -> *Preference* under *System Settings*. This helps
    - To program the Usecase prototyping kit to factory reset application by TPDS
    - To open the embedded project of the Usecase
 - Note that *~/.trustplatform/spg_firm_validation* is the **Usecase working directory**. It contains the resources generated during transaction diagram execution.
    - ~ indicates home directory.
        - Windows home directory is \user\username
        - Mac home directory is /users/username
        - Most Linux/Unix home directory is /home/username
 - Build Firmware validation application
   - Open the embedded project by clicking *MPLAB X Project* button on the Usecase diagram
     - Set the project as Main -> right click on Project and select *Set as Main Project*
     - Set the configuration -> right click on Project, expand *Set Configuration* to select *default*
     - Build the project -> right click on project and select *Clean and Build*.
   - On Build completion, generated hex file should be available in this Usecase folder
 - Build an application with adjusted start address. Below are the steps for IP Protection application as example
    - Run the IP Protection Usecase and launch embedded project
    - Once the Usecase project is loaded on MPLAB X IDE,
        - Set the project as Main -> right click on Project and select *Set as Main Project*
        - Set the configuration -> right click on Project, expand *Set Configuration* to select *FIRMWARE_VALIDATION*
        - Build the project -> right click on Project and select *Clean and Build*
          - Generate hex file will be copied to Firmware validation Usecase folder
    - On Build completion, start address adjusted hex file should be available in this Usecase (Firmware validation) folder

## Post Usecase transaction Steps
On completing Usecase steps execution on TPDS, the combined hex file is programmed to development kit. it is possible to view C source files by clicking *C Source Folder* button.

- Log from the combined hex file can be viewed using applications like TeraTerm. Select the COM port and set baud rate as 115200-8-N-1

