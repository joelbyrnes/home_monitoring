import serial
import time
import os

#SERIAL_PORT = "/dev/ttyUSB0"
SERIAL_PORT = os.environ["SERIAL_PORT"]

def main():
	port = None
	try:
		port = serial.Serial(SERIAL_PORT, 57600, timeout=300)
		print port.portstr
		#time.sleep(2)
		while 1:
			data = port.readline()
			print data,
	except KeyboardInterrupt:
		print '^C received, exiting.'
		port.close()

if __name__ == '__main__':
    main()

