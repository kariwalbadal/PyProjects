import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time
import os

blocksize = 1024

SERVER_IP   = '192.168.1.103'
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))
i=0
mySocket = socket( AF_INET, SOCK_DGRAM )

if os.path.exists('GOT_704_mp4.mp4'):
	with open('GOT_704_mp4.mp4', 'rb') as f:
		packet = f.read(blocksize)
		while packet != '' :
			mySocket.sendto(packet,(SERVER_IP,PORT_NUMBER))
			packet = f.read(blocksize)
			time.sleep(0.002)
sys.exit()