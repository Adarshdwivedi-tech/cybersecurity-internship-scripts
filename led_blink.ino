/*
  Multi-LED Blink (Alternating Pattern)
  ----------------------------------------
  Controls 3 LEDs connected to digital pins 3, 4, and 5 on an Arduino Uno.
  The LEDs alternate between two states every 1 second, creating a simple
  blinking pattern.

  Circuit:
    - LED 1 -> Pin 4 (+ resistor to GND)
    - LED 2 -> Pin 5 (+ resistor to GND)
    - LED 3 -> Pin 3 (+ resistor to GND)

  Built and simulated in Tinkercad, then tested on real Arduino Uno
  hardware with a single LED (pin-based logic identical, simplified
  circuit).
*/

void setup()
{
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  // State 1: LEDs on pins 4 and 5 ON, pin 3 OFF
  digitalWrite(4, HIGH);
  digitalWrite(3, LOW);
  digitalWrite(5, HIGH);
  delay(1000); // Wait for 1000 milliseconds (1 second)

  // State 2: LEDs on pins 4 and 5 OFF, pin 3 ON
  digitalWrite(4, LOW);
  digitalWrite(3, HIGH);
  digitalWrite(5, LOW);
  delay(1000); // Wait for 1000 milliseconds (1 second)
}
