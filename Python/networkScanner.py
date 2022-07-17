#!/user/bin/env python

# Look into scapy.ls scapy.showb

from scapy.all import arping

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")	# ff: is the broadcast
	arp_request_broadcast = broadcast/arp_request
	answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout = 1)

scan("10.")