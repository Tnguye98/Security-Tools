#!/usr/bin/env python3

import subprocess

print("[~] Running the command `ifconfig`.")

subprocess.call("ifconfig", shell = True)

interface = input("interface >")
new_mac = input("new MAC >")

print("[+] Changing MAC address for:\n" + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell = True)
subprocess.call("ifconfig hw ether " + new_mac, shell = True)
subprocess.call("ifconfig " + interface +" up", shell = True)