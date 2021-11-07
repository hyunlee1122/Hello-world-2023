// demonstrates sending a value from an arduino to p5js
// which inicates the position of a potentiometer connected to pin A0


const int potPin = A0; // pin the pot is connected to
int potVal = 0; // variable to hold the value from the sensor

void setup() {
  
  // initialize the serial communication:
  Serial.begin(9600);
}

void loop() {
  // read the value of the pot and store it
  potVal = analogRead(potPin);

  // write the value out to the serial port
  Serial.println(potVal);
  
  // wait a bit for between readings
  delay(10);
}
