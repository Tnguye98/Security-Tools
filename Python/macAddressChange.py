#!/usr/bin/env python3

import subprocess				# Used for commands
import optparse					# Used for arguments : this is depreicated (argparse)
import re						# Used to filter strings Use: pythex.org 		

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC address")
	parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please an interface, use --help for more info.")
	elif not options.new_mac:
		parser.error("[-] Please an new mac, use --help for more info.")
	return options

def change_mac(interface, new_mac):
	print("[+] Changing MAC address for: " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
	ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
	mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

	if mac_address_search_result:
		return mac_address_search_result.group(0)
	else:
		print("[-] Could not read MAC address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))

# change_mac(interface = options.interface, new_mac = options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
	print("[+] MAC address was successfully changed to " + current_mac)
else:
	print("[-] MAC addresss did not get changed.")