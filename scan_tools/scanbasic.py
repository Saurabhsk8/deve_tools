#!/usr/bin/python3

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ad_net = ipv4,sock_stream=tcp packet
socket.setdefaulttimeout(30) #to timeout scaning after certain time

host = input('[*] Enter the host to scan: ')
#port = int(input('[*] Enter the port to scan: '))

#host = "192.168.1.4"
#port = 111

def portscanner(port):
    if sock.connect_ex((host, port)):
        print(colored('Port %d is closed' %(port), 'red'))
    else:
        print(colored('Port %d is open' %(port), 'green'))

for port in range(1,1000):
    portscanner(port)