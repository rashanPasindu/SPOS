import nmap
import sys
import socket

import sendDataTOdb as db


def initiate_scan(ip):
    scan(ip)


# ipaddress = sys.argv[1]
# portrange = sys.argv[2]

# ipaddress = socket.gethostbyname(hostaddress)  # translate hostname into ipv4 address


def scan(ip):
    scanType = 'NMAP'
    hostaddress = ''
    ipaddress = ip
    portrange = '100-10000'

    print("----------" * 6)
    print("       Please Wait, Scanning The Host " + ipaddress)
    print("----------" * 6)

    try:
        # initialize the port scanner
        nmScan = nmap.PortScanner()  # instantiate nmap.PortScanner object
        nmScan.scan(ipaddress, portrange)  # scan host which is specify & ports from 22 to 44
    except nmap.PortScannerEror:
        print('Nmap not found', sys.exc_info()[0])
        sys.exit(0)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(0)

    # run a loop to print all the found result about the ports
    for host in nmScan.all_hosts():
        print("       Host : %s (%s)" % (host, hostaddress))
        print("       State : %s" % nmScan[host].state())  # get state of host(up|down|unknown|skipped)
        # take the host for host address
        state = nmScan[host].state()
        # now write the loop for finding the protocol
        # now write the loop for finding the protocol
        for proto in nmScan[host].all_protocols():  # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
            print("----------" * 6)
            print("       Protocol : %s" % proto)
            # get protocol from proto
            lport = nmScan[host][proto].keys()  # get all ports for tcp/udp protocol
            sorted(lport)
            for port in lport:
                print("       port : %s\tstate : %s" % (port, nmScan[host][proto][port]['state']))
                portstate = nmScan[host][proto][port]['state']
                db.sendTODB(host, state, port, portstate, scanType)