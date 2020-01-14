#!/usr/bin/python3

from socket import *
import optparse
from threading import *

def connScan(target_host, target_port):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((target_host, target_port))
        print('[+] %d/tcp open' %target_port)
    except:
        print('[+] %d/tcp closed' %target_port)
    finally:
        sock.close()

def portscan(target_host, target_port):
    try:
        target_ip = gethostbyname(target_host) #convert hostname(google.com) to ip
    except:
        print('UNKNOWN HOST %s' %target_host)

    try:
        target_name = gethostbyaddr(target_ip) #gets host name from address
        print('[+]Scan Results for: ' +target_name[0])
    except:
        print('[+]Scan result for: ' +target_ip)
    setdefaulttimeout(10)

    #to scan all the ports provided by users
    for target_ports in target_port: #scanning all the ports through threading
        t = Thread(target=connScan, args=(target_host, int(target_ports)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='target_host', type='string', help='specify target host')
    parser.add_option('-p', dest='target_port', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()

    target_host = options.target_host
    target_port = str(options.target_port).split(',')

    if (target_host == None) | (target_port[0] == None): #[0] cause its list
        print(parser.usage)
        exit(0)
    portscan(target_host, target_port)

if __name__ == '__main__':
    main()