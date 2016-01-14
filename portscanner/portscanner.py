import socket
import subprocess
import sys
from datetime import datetime

remoteServer = 'www.gazzetta.it'
remoteServerIP = socket.gethostbyname(remoteServer)

start_time = datetime.now()
common_ports = {
	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'389': 'LDAP',
	'443': 'HTTPS',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'2082': 'CPANEL',
	'2083': 'CPANEL',
	'3306': 'MYSQL',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}

for port in sorted(common_ports):
    port = int(port)
    print 'scanning port %i' % port
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP,port))
    print 'Port %i: \t%i' %(port,result)
    sock.close()