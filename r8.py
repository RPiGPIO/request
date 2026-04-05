# PRACTICAL 8 - FLAME SENSOR WITH LED ALERT
# File: practical_8_flame_sensor.py

# =====================================
# PIN CONNECTIONS
# =====================================
# Flame Sensor VCC -> 3.3V -> Pin 1
# Flame Sensor GND -> GND -> Pin 6
# Flame Sensor DO  -> GPIO17 -> Physical Pin 11
# LED Positive     -> GPIO18 -> Physical Pin 12
# LED Negative     -> GND -> Pin 14

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect flame sensor VCC and GND
# 2. Connect DO pin to GPIO17
# 3. Connect LED positive to GPIO18 using resistor
# 4. Connect LED negative to GND
# 5. Run code and bring lighter flame near sensor

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Library: RPi.GPIO
# Install if needed:
# sudo apt install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

FLAME = 17
LED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

try:
    while True:
        if GPIO.input(FLAME) == 0:
            print("🔥 Flame Detected")
            GPIO.output(LED, GPIO.HIGH)
        else:
            print("No Flame")
            GPIO.output(LED, GPIO.LOW)

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
