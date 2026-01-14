#include <Servo.h>

Servo myservo;  
const int ldrPin = A0;   
const int servoPin = 9;   
int ldrValue = 0;         
int servoAngle = 0;       

void setup() {
  myservo.attach(servoPin); 
  Serial.begin(9600);        
}

void loop() {
  ldrValue = analogRead(ldrPin);
  servoAngle = map(ldrValue, 0, 1023, 15, 0);
  servoAngle = constrain(servoAngle, 0, 15);
  myservo.write(servoAngle);
  Serial.print("LDR Value: ");
  Serial.print(ldrValue);
  Serial.print("\t Servo Angle: ");
  Serial.println(servoAngle);
  
  delay(100); 
}
