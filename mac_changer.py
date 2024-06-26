#!/usr/bin/env python3

import subprocess
import optparse

def get_arguements():
	parser = optparse.OptionParser()
        parser.add_option("-i", "--interface", dest="interface", help="interface to change the MAC Address")
        parser.add_option("-m", "--mac", dest="new_mac", help="new MAC Address")
        (options, arguements) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an interface, use --help for more info.")
	elif not options.new_mac:
		parser.error("[-] Please specify a MAC, use --help for more info.")
	return options


def change_mac(interface, new_mac):
	print("[+] Changing mac address for " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])
 


if __name__ == '__main__':
	options = get_arguements()
	change_mac(options.interface, options.new_mac)
