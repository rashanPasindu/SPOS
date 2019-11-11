import nmap
import sys
import socket
import xlwt
from xlwt import Workbook
from datetime import date as date1
import dbconnect as db

wrkbk = Workbook()


# if len(sys.argv) != 3:
#    print("Usage: ./port.py <Host_Address> <Port_Range>")
#   sys.exit(0)


# def createReport(ip, data, iterative):
# sheet1 = wrkbk.add_sheet('Nmap Scan Results for IP: ' + ip)

# if sheet1 is not None:
# sheet1.write(iterative, )


def initiate_scan(ip):
    scan(ip)


# ipaddress = sys.argv[1]
# portrange = sys.argv[2]

# ipaddress = socket.gethostbyname(hostaddress)  # translate hostname into ipv4 address

def editDate():
    dat = date1.today()
    dat = dat.strftime('%Y-%m-%d')
    return dat


def sendTODB(ip, state, ports, daten):
    conn = db.getcon()
    cursor = conn.cursor()
    scabType = 'NMAP'

    try:
        query = "INSERT INTO scan_results (scan_type, scanned_ip, state, ports_open, datentime) VALUES (%s, %s, %s, " \
                "%s, %s) "
        values = (scabType, ip, state, ports, daten)
        cursor.execute(query, values)
        conn.commit()

        if cursor.lastrowid:
            print('last insert id: ', cursor.lastrowid)
        else:
            print('no last insert id found')

        print("Data Sent to database")
    except db.Error as error:
        print(error)
    finally:
        db.destroyConn()

        
def scan(ip):
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
        # now write the loop for finding the protocol

        for proto in nmScan[host].all_protocols():  # get all scanned protocols ['tcp', 'udp'] in (ip|tcp|udp|sctp)
            print("----------" * 6)
            print("       Protocol : %s" % proto)

            lport = nmScan[host][proto].keys()  # get all ports for tcp/udp protocol
            sorted(lport)
            for port in lport:
                print("       port : %s\tstate : %s" % (port, nmScan[host][proto][port]['state']))
