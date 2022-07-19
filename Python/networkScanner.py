#!/user/bin/env python

# Look into scapy.ls

from scapy.all import arping
import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest = "target", help = "The ip address of the target machine.")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")	# ff:.. is the broadcast mac
	arp_request_broadcast = broadcast / arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]

	clients_list = []
	for element in answered_list:
		client_dict = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
		clients_list.append(client_dict)
	return clients_list

def print_result(results_list):
	print("IP\t\t\tMAC Address\n--------------------------------------------------")
	for client in results_list:
		print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result_arg = scan(options.target())
scan_result = scan("10.10.0.6/24")
print_result(scan_result)