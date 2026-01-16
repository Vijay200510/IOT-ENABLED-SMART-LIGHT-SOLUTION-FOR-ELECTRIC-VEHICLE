IoT Enabled Smart Light Solution for Electric Vehicle
Abstract

This project focuses on the development of an adaptive headlight system that automatically adjusts the beam intensity and direction of vehicle headlights in real time. Using a Light Dependent Resistor (LDR) to detect glare from oncoming vehicles, a microcontroller (Arduino Uno) processes the data and controls a servo motor and LED headlight module to minimize glare and improve road safety. The solution is low-cost, efficient, and suitable for smart and electric vehicles.

Objectives

Reduce nighttime road accidents caused by headlight glare

Improve visibility without driver intervention

Design a cost-effective adaptive lighting system

Ensure compatibility with modern automotive platforms

Problem Statement

Conventional vehicle headlight systems operate at fixed beam angles and intensities, which do not adapt to changing traffic or lighting conditions. This results in excessive glare for oncoming drivers, temporary vision impairment, and increased accident risk. The proposed system addresses these issues by dynamically controlling headlight behavior based on real-time light detection.

System Components

LDR (Light Dependent Resistor): Detects ambient and oncoming light intensity

Arduino Uno: Acts as the central processing unit

Servo Motor: Adjusts headlight beam angle

LED Headlight Module: Controls light intensity using PWM

Power Supply (12V DC): Vehicle-compatible input

Buck Converter: Steps down voltage to 5V for electronics

Working Principle

LDR continuously monitors incoming light intensity

Arduino compares sensor values with a preset threshold

If glare is detected:

Servo motor tilts the headlight downward

LED brightness is reduced

Once glare disappears:

Beam angle and brightness are restored

System Operation

Continuous light monitoring using LDR sensors

Analog data processed by Arduino ADC

Threshold-based decision making

Servo motor and LED respond in real time

System resets to default state after glare removal

System Design
Circuit Design

LDR connected to Arduino analog pin

Servo motor controlled via PWM pin

LED brightness controlled using PWM output

Mechanical Design

Headlight casing mounted on servo-controlled brackets

Compact and protected internal assembly

Software Logic

Programmed in Arduino C/C++

Uses real-time sensor mapping and servo control

Software Code (Arduino)
#include <Servo.h>
Servo myservo;

const int ldrPin = A0;
const int servoPin = 9;

void setup() {
  myservo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  int ldrValue = analogRead(ldrPin);
  int servoAngle = map(ldrValue, 0, 1023, 15, 0);
  servoAngle = constrain(servoAngle, 0, 15);
  myservo.write(servoAngle);
  delay(100);
}

Implementation

All components integrated inside the headlight enclosure

LDR sensors mounted to detect oncoming light effectively

Servo motor fixed to reflector/LED bracket

Buck converter provides stable 5V supply

Environmental Protection

IP65-rated sealed enclosure

UV-resistant transparent shielding on sensors

Drain holes and ventilation mesh for moisture control

Limitations

Most effective when both vehicles use adaptive headlights

Sensor performance affected by fog, rain, or snow

Requires periodic calibration

Heat and space constraints inside headlight housing

Advantages

Reduces glare for oncoming drivers

Improves nighttime road safety

Automatic operation without driver input

Low-cost and scalable solution

Suitable for electric and smart vehicles

Conclusion

The IoT Enabled Smart Light Solution provides a practical and affordable approach to addressing nighttime driving hazards. By combining light sensors, microcontroller logic, and mechanical actuation, the system enhances road safety and demonstrates strong potential for future automotive applications.

Author

Vijay Banasiya
Mechanical Engineering Student
