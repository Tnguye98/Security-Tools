#!/usr/bin/env python3

import subprocess
import optparse

def change_mac(interface, new_mac):
	print("[+] Changing MAC address for: " + interface + " to " + new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])


print("[~] Running the command `ifconfig`.")
subprocess.call("ifconfig", shell = True)

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change its MAC address")
parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address")
(options, arguments) = parser.parse_args()

change_mac(interface = options.interface, new_mac = options.new_mac)