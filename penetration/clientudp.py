import socket

host = '127.0.0.1'
port = 12345


class ClientUDP:
	def __init__(self):
		self.s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	def connect(self):
		print self.s.sendto('This',(host,port))

if __name__ == '__main__':
	client = ClientUDP()
	client.connect()