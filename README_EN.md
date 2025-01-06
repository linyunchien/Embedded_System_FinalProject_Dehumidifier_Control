# Servo Motor and Humidity Control System

## Overview

This project integrates Arduino and a PyQt5 application to monitor the environment using a humidity sensor and control a servo motor to operate a dehumidifier. The system provides manual and automatic mode switching.

## Features

1. **Manual Servo Control**: Trigger the servo motor through a GUI button.
2. **Automatic Dehumidifier Control**: Automatically triggers the servo motor when humidity exceeds a specified threshold.
3. **Humidity Monitoring**: Displays the current environmental humidity in real time within the GUI.

## Hardware Requirements

- Arduino board (e.g., Uno)
- Servo motor
- DHT11 or DHT22 humidity and temperature sensor
- USB cable for connecting the Arduino to a computer
- A computer with Python installed

## Software Requirements

1. **Python Packages**:

   - PyQt5
   - pyserial

   Install using the following command:

   ```bash
   pip install PyQt5 pyserial
   ```

2. **Arduino Libraries**:

   - DHT sensor library by Adafruit

   Installable via the Arduino IDE Library Manager.

## Setup Steps

### Arduino

1. Connect the servo motor signal pin to pin 9 on the Arduino.
2. Connect the DHT sensor data pin to pin 2 on the Arduino.
3. Upload the provided Arduino code to the Arduino board.

### Python Application

1. Ensure the Arduino is connected to the computer and note its COM port (e.g., `COM3`).
2. Update the COM port setting in the Python code to match the Arduino.
3. Run the Python script:
   ```bash
   python servo_control.py
   ```

## Usage Instructions

1. **Manual Mode**:
   - Click the "Press Servo (Manual)" button in the GUI to manually trigger the servo motor.
2. **Automatic Mode**:
   - Check the "Automatic Dehumidifier Control" box to enable automatic mode.
   - The servo motor will automatically trigger when humidity exceeds 60%, and reset once the humidity drops below the threshold.
3. **Humidity Monitoring**:
   - The GUI displays the current humidity in real time.

## Troubleshooting

1. **Humidity Not Displayed**:

   - Ensure the DHT sensor is properly connected.
   - Verify that the Arduino is running correctly and the COM port is set correctly.

2. **Servo Motor Not Responding**:

   - Check if the servo motor is correctly connected.
   - Ensure the servo motor pin in the Arduino code matches the hardware setup.

3. **Invalid Data Received**:

   - Ensure the sensor type (DHT11 or DHT22) in the Arduino code matches your hardware.
   - Check for loose connections.

## Customization

- Modify the `thresholdHumidity` variable in the Arduino code to change the humidity threshold.
- Adjust the GUI layout or add new features by modifying the Python code.


