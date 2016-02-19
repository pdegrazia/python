import socket

class Client:
	def __init__(self):
		self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	def connect(self,address,port):
		self.s.connect((address,port))
		buff = bytearray('-'*30)

		print 'Number of bytes:',self.s.recv_into(buff)
		print buff
		self.s.close()

if __name__ == '__main__':
	client = Client()
	client.connect('127.0.0.1',12345)