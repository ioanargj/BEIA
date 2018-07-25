from time import sleep
from random import randint
import argparse
import socket
import time

SERVER='graphite.beia-telemetrie.ro'
PORT=2003

sock = socket.socket()
sock.connect((SERVER, PORT))
if __name__ == '__main__':
	while True:

    		timestamp=int(time.time())
    		metrics='ioana.rpi.random'
    		value=randint(0,10)
    		message='%s %s %d\n' % (metrics, value, timestamp)
    		print 'sending message:\n' + message
    		sock.sendall(message)
    	sleep(60)
sock.close()
