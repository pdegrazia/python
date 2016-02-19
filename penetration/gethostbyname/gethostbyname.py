import socket

class DomainResolver:
	def __init__(self):
		pass

	def connect(self, host):
		print socket.gethostbyname(host)
		return

	def connect_ex(self,host):
		hosts = socket.gethostbyname_ex(host)[2]
		print 'Hosts:'
		print ';'.join(hosts[2])
		return

if __name__ == '__main__':
	dr = DomainResolver()
	dr.connect('www.google.com')
	dr.connect_ex('www.gazzetta.it')