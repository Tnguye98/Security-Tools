#!/usr/env/bin python3

import scapy.all as scapy

def getMAC(ip):
	arpRequest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest
	answeredList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]

	return answeredList[0][1].hwsrc

def sniff(interface):
	scapy.sniff(iface = interface, store = False, prn = processSniffedPacket)

def processSniffedPacket(packet):
	if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
		try:
			realMAC = getMAC(packet[scapy.ARP].psrc)
			responseMAC = packet[scapy.ARP].hwsrc

			if realMAC != responseMAC:
				print("[+] You are under attack!")
		except IndexError:
			pass

sniff("eth0")