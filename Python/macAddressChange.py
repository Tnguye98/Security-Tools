#!/usr/bin/env python3

import subprocess
import optparse

print("[~] Running the command `ifconfig`.")

subprocess.call("ifconfig", shell = True)

interface = input("interface >")
new_mac = input("new MAC >")

print("[+] Changing MAC address for: " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether"])
subprocess.call(["ifconfig", interface, "up"])