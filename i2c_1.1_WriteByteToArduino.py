
# https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi

from smbus2 import SMBus
from time import sleep
		
		
def main():

	#  MCP4725 defaults to address 0x60
	address = 0x7f

	# Initialize I2C (SMBus)
	bus = SMBus(1)
	
	#bus.write_byte(address, 0x01)
	byte_to_send = 0;
	
	'''
		Values greater than a byte, 0-255, are overflowed back around.
		For example, sending 256 results in a 0, 257 -> 1, etc.
	'''
	
	while byte_to_send <=255:
		print("Writing", byte_to_send)
		try:
			bus.write_byte(address, byte_to_send)
			byte_to_send += 1
		except OSError:
			print("OSError: Failed to write to specified peripheral")
		sleep(.2)
		
		'''
		print("Writing 0")
		try:
			bus.write_byte(address, 0x00)
		except OSError:
			print("OSError: Failed to write to specified peripheral")
		sleep(1)
		'''

if __name__ == '__main__':
	main()
		