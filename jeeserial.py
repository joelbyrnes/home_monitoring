import serial
import time

SERIAL_PORT = "/dev/tty.usbserial-A600dVGp"

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

