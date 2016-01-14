import socket
import subprocess
import sys
from datetime import datetime

remoteServer = 'www.gazzetta.it'
remoteServerIP = socket.gethostbyname(remoteServer)

start_time = datetime.now()

for port in range(1,1024):
    print 'scanning port %i' % port
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result = sock.connect_ex((remoteServerIP,port))
    print 'Port %i: \t%i' %(port,result)
    sock.close()