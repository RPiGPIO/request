# PRACTICAL 6 - IR SENSOR WITH LED ALERT
# File: practical_6_ir_sensor.py

# =====================================
# PIN CONNECTIONS
# =====================================
# IR Sensor OUT -> GPIO23 -> Physical Pin 16
# IR Sensor VCC -> 5V -> Pin 2
# IR Sensor GND -> GND -> Pin 6
# LED Positive  -> GPIO24 -> Physical Pin 18
# LED Negative  -> GND -> Pin 14

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect IR sensor VCC to 5V
# 2. Connect GND to Raspberry Pi GND
# 3. Connect OUT pin to GPIO23
# 4. Connect LED positive to GPIO24 with resistor
# 5. Connect LED negative to GND
# 6. Run the code and place object near sensor

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Library: RPi.GPIO
# Install if needed:
# sudo apt install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

IR = 23
LED = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(IR) == 0:
            print("Object Detected")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("No Object")
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
