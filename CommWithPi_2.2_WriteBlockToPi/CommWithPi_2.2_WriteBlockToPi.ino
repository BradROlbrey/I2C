
#include <Wire.h>

byte moving = 1;
byte move_array[10];

void setup() {
  Wire.begin(0x7f);               // Join i2c bus with address
  Wire.onRequest(requestEvent);   // Register event for sending data to master upon request
  
  Serial.begin(9600);             // Start serial for output
  //while ( !Serial ) ;

  for (int i = 0; i < 10; ++i)
    move_array[i] = 0;
  
}

void loop() {
 delay(500);
}

void requestEvent() {
  delayMicroseconds(8);
  Wire.write(move_array, 10);             // Respond with status update, completed moving or not.

  for (int i = 0; i < 9; ++i)
    move_array[i] = move_array[i+1];
  move_array[9] = moving++;
}
