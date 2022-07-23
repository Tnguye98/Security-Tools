#!/usr/bin/env python 3
import scapy.all as scapy
import optparse


def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Target IP / IP range.")
    options, arguments = parser.parse_args()
    
    return options

def scan(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcast = broadcast/arpRequest
    answeredList = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
    
    clientsList = []
    for element in answeredList:
        clientDict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clientsList.append(client_dict)
    
    return clientsList

def printResult(results_list):
    print("IP\t\t\tMAC Address\n--------------------------------------------------")
    for client in resultsList:
        print(client["ip"] + "\t\t" + client["mac"])


options = get_arguments()
scanResult = scan(options.target)
printResult(scanResult)