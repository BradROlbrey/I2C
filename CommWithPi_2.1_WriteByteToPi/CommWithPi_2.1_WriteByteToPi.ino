// Wire Slave Sender
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Sends data as an I2C/TWI slave device
// Refer to the "Wire Master Reader" example for use with this

// Created 29 March 2006

// This example code is in the public domain.

byte to_send = 1;

#include <Wire.h>

void setup() {
  Wire.begin(0x7f);                // join i2c bus with address
  Wire.onRequest(requestEvent); // register event
}

void loop() {
  delay(100);
}

// function that executes whenever data is requested by master
// this function is registered as an event, see setup()
void requestEvent() {
  delayMicroseconds(8);  // With a frequency of 8us, an 8us delay seems to work pretty swell.
  Wire.write(to_send);

  to_send <<= 1;
  if (to_send == 0)
    to_send = 1;
}
