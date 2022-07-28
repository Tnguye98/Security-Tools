#!/usr/bin/env python3
import netfilterqueue
import scapy.all as scapy


def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	if scapyPacket.haslayer(scapy.Raw):
		if scapyPacket[scapy.TCP].dport == 80:
			print("HTTP Request")
			print(scapyPacket.show())
		elif scapyPacket[scapy.TCP].sport == 80:
			print("HTTP Response")
			print(scapyPacket.show())

	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()