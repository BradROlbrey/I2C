
# https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial/all#i2c-on-pi

from smbus2 import SMBus
from time import sleep
		
		
def main():

	#  MCP4725 defaults to address 0x60
	address = 0x7f

	# Initialize I2C (SMBus)
	bus = SMBus(1)
	
	'''
		For some reason, sends the offset/register as if it was at the head
		of the data array.
	'''
	while True:
		print("Writing 1")
		try:
			bus.write_i2c_block_data(address, 5, [1,1,0,0,1,1,0,0])
		except OSError:
			print("OSError: Failed to write to specified peripheral")
		sleep(1)
		
		print("Writing 0")
		try:
			bus.write_i2c_block_data(address, 1, [0,0,1,1,0,0,1,1])
		except OSError:
			print("OSError: Failed to write to specified peripheral")
		sleep(1)


if __name__ == '__main__':
	main()
		