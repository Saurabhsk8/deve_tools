#!/usr/bin/python3

from socket import *

def GetBanner(ip, port):
    try:
        setdefaulttimeout(2)
        s = socket()
        s.connect((ip, port))
        banner = s.recv(1024) #recv = recive 1024 bytes from target
        return banner
    except:
        return

def main():
    #port = 22
    ip = input('[+] Target ip:')
    for port in range(1, 100):
        banner = GetBanner(ip, port)
        if banner:
            print("[+]" + ip +" / "+ str(port) +": " + banner.decode().strip('/n'))

main()