import socket # Using the socket library
import time
host = "127.0.0.1" # stating the host
port = 5000 # stating the port number

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating a new socket object
s.bind((host,port)) # binding the tuple of (host,port) to the socket object s
s.setblocking(0)

quitting = False
print "Server Started"
	
while not quitting:
	try:
		data, addr = s.recvfrom(1024)
		if "Quit" in str(data):
			quitting = True
		if addr not in clients:
			clients.append(addr)
			
		print time.ctime(time.time()) + str(addr) + ": :" + str(data)
		for client in clients:
			s.sendto(data, client)
	except:
		pass
		
s.close()
