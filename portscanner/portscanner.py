import socket
from datetime import datetime
from resources import *


class PortScanner:
    def __init__(self):
        self.server_list = server_list
        self.ports = common_ports.keys()
        socket.setdefaulttimeout(0.5)

    def print_ports_to_scan(self):
        for port in self.ports:
            print port

    def print_servers_to_scan(self):
        for server in self.server_list:
            print server

    def start_scanning(self):
        for server in self.server_list:
            print 'Scanning Server %s:' % server
            print 'Resolving host...'
            server_ip = self.resolve_name(server)
            print 'Server hosted on %s' % str(server_ip)
            for port in self.ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                start = datetime.now()
                result = self.check_port(sock, server_ip, port)
                if result == 0:
                    print 'Port %s opened!' % port
                elapsed_time = datetime.now() - start
                sock.close()
                print 'Elapsed time: %s' % str(elapsed_time)

    def check_port(self, sock, server, port):
        return sock.connect_ex((server, int(port)))

    def resolve_name(self, server_name):
        return socket.gethostbyname(server_name)


class PortListener(PortScanner):
    def __init__(self):
        PortScanner.__init__(self)

    def listen_on_port(self, port):
        self.sock.bind((port, server_list[0]))
        self.sock.listen(5)


if __name__ == '__main__':
    ps = PortScanner()
    ps.start_scanning()

    # pl = PortListener()
    # pl.listen_on_port(80)
