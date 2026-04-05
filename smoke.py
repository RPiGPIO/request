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

# PRACTICAL 10 - SMOKE SENSOR WITH LED ALERT
# Smoke Sensor DO -> GPIO17 -> Pin 11
# LED -> GPIO27 -> Pin 13
# GND -> Pin 6
# 5V -> Pin 2

import RPi.GPIO as GPIO
import time

SMOKE_DO = 17
LED_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(SMOKE_DO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Smoke sensor warming up... wait 20 seconds")
GPIO.output(LED_PIN, GPIO.LOW)
time.sleep(20)

print("System Ready")
print("Monitoring smoke/gas...")

try:
    while True:
        smoke_detected = (GPIO.input(SMOKE_DO) == 0)

        if smoke_detected:
            print("🚨 SMOKE/GAS DETECTED")
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            print("Air is clean")
            GPIO.output(LED_PIN, GPIO.LOW)

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()