# PRACTICAL 3 - TWO LED CONTROL WITH PYTHON
# File: practical_3_two_led.py

# =====================================
# PIN CONNECTIONS
# =====================================
# LED 1 -> GPIO22 -> Physical Pin 15
# LED 2 -> GPIO23 -> Physical Pin 16
# Both negatives -> GND Pin 6 / 9

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect LED1 positive to GPIO22 via 330 ohm resistor
# 2. Connect LED2 positive to GPIO23 via 330 ohm resistor
# 3. Connect both LED negatives to GND
# 4. Power ON Raspberry Pi

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Library: RPi.GPIO
# Install if needed:
# sudo apt install python3-rpi.gpio

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED1 = 22
LED2 = 23

GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

try:
    while True:
        GPIO.output(LED1, GPIO.HIGH)
        GPIO.output(LED2, GPIO.LOW)
        time.sleep(1)

        GPIO.output(LED1, GPIO.LOW)
        GPIO.output(LED2, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
