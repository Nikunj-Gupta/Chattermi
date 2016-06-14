import socket
import threading
import time

# Multithreading Used here for all clients
tLock = threading.Lock()
shutdown = False

def recieving(name, sock):
	while not shutdown:
		try:
			tLock.acquire()
			while True:
				data, addr = sock.recvfrom(1024)
				print str(data)
		except:
			pass
		finally:
			tLock.release()
			
host = "127.0.0.1"
port = 0 # Different port number because we are technically setting up another server

server = ("127.0.0.1", 5000)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

rT = threading.Thread(target = recieving, args = ("RecvThread",s))
rT.start()

name = raw_input("Name: ")
message = raw_input(name + ": ")

while (message != 'q'):
	if message != "":
		s.sendto(message, server)
	tLock.acquire()
	message = raw_input(name + ": ")
	tLock.release()
	time.sleep(0.2)
	
shutdown = True
rT.join()
s.close()
