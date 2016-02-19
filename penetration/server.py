import socket

class Server:

	def __init__(self,server_type='normal'):
		self.connection = 0
		self.address = '127.0.0.1'
		self.port = 12345
		self.s = self._setup_socket(server_type)
		self._setup_connection()

	def _setup_socket(self,server_type):
		if server_type == 'normal':
			return socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		elif server_type == 'udp':
			return socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		else:
			pass

	def _setup_connection(self):
		self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.s.bind((self.address,self.port))
		print 'Server running on %s:%s' % (self.address,self.port)

	def start(self):
		self.s.listen(2)
		while True:
			conn, addr = self.s.accept()
			if conn:
				self.connection+=1
			print addr, 'now connected'
			print 'Connection #'+str(self.connection)
			conn.send('Porca madonna,request #'+str(self.connection))
			conn.close()

if __name__ == '__main__':
	server = Server('normal')
	server.start()
