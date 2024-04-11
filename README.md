# MAC Address Changer

This simple Python script allows you to quickly change the MAC address of a network interface on Linux systems.

Usage
Clone this repository:

Bash
git clone https://github.com/RahulKrSahu/mac-changer
Use code with caution.
Navigate to the project directory:

Bash
cd mac-changer
Use code with caution.
Run the script with the required arguments:

Bash
python main.py -i <interface> -m <new_mac_address>
Use code with caution.
Replace <interface> with the name of the network interface you want to modify (e.g., eth0, wlan0) and <new_mac_address> with the desired MAC address.

Example
To change the MAC address of the eth0 interface to 00:11:22:33:44:55, you would run:

Bash
python main.py -i eth0 -m 00:11:22:33:44:55
Use code with caution.
Requirements
Python 3
Linux operating system
Permissions
This script requires administrative privileges to modify network interfaces. Ensure you run it with sudo or as a root user.

Notes
Exercise caution when changing MAC addresses, as it can affect network connectivity.
The script utilizes the ifconfig command, which may be deprecated on some systems. Consider alternative methods for more recent Linux distributions.
Contributing
Pull requests are welcome! If you have suggestions for improvements or bug fixes, please feel free to contribute to the project.

License
This project is licensed under the MIT License.
