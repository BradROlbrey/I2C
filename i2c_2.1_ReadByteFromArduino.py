
# https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi

from smbus2 import SMBus
from time import sleep
		
		
def main():
	
	# Initialize I2C (SMBus)
	bus = SMBus(1)
	arduino_addr = 0x7f
	
	arduino_status = -1
	
	while arduino_status < 255:
		
		try:
			print("Requesting status: ", end='')
			arduino_status = bus.read_byte(arduino_addr)
			#print(type(bus.read_byte(arduino_addr)))
		except OSError:
			print("OSError: Failed to read from specified peripheral")
			
		print("status:", arduino_status)
		sleep(.05)  # Take a picture


if __name__ == '__main__':
	main()
		