import socket
from netaddr import *


def scan_port(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)
    try:
        connect = sock.connect((ip, 80))
        connect.close()
        print(ip, "is available")
    except:
        print(ip, "is not available")


#ip = '109.194.17.1'
ipStart, ipEnd = input("Enter IP-IP: ").split("-")
iprange = IPRange(ipStart, ipEnd)

for ip in iprange:
    host = str(ip)
    scan_port(host)
