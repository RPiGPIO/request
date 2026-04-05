# PRACTICAL 10 - SMOKE SENSOR WITH LED ALERT
# File: practical_10_smoke_sensor.py

# =====================================
# PIN CONNECTIONS
# =====================================
# Smoke Sensor VCC -> 5V -> Pin 2
# Smoke Sensor GND -> GND -> Pin 6
# Smoke Sensor DO  -> GPIO17 -> Physical Pin 11
# LED Positive     -> GPIO27 -> Physical Pin 13
# LED Negative     -> GND -> Pin 14

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect MQ sensor VCC to 5V
# 2. Connect GND to Raspberry Pi GND
# 3. Connect DO pin to GPIO17
# 4. Connect LED positive to GPIO27 via resistor
# 5. Connect LED negative to GND
# 6. Run code and bring smoke near sensor

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Library: RPi.GPIO
# Install if needed:
# sudo apt install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

SMOKE = 17
LED = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(SMOKE, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(SMOKE) == 0:
            print("🚨 Smoke Detected")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("Air Clean")
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
