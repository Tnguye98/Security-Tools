#!/user/bin/env python

# Look into scapy.ls

from scapy.all import arping

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")	# ff:.. is the broadcast mac
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

	print("IP\t\t\tMAC Address\n--------------------------------------------------")
	for element in answered_list:
		print(element[1].psrc + "\t\t" + element[1].hwsrc)

scan("10.10.0.6/24")