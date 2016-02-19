import socket
from server import Server

class ServerUDP(Server):

	def __init__(self,server_type):
		Server.__init__(self,server_type=server_type)

	def start(self):
		self.s.settimeout(15)
		while True:
			data,addr = self.s.recvfrom(1024)
			print 'Incoming connection from ', addr
			print 'Received: ',data
			self.s.close()

if __name__ == '__main__':
	serverUDP=ServerUDP('udp')
	serverUDP.start()