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

FLAME_DO = 17
ALERT = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_DO, GPIO.IN)
GPIO.setup(ALERT, GPIO.OUT)

GPIO.output(ALERT, False)

print("Flame Sensor Ready... Press CTRL+C to stop")

try:
    while True:
        value = GPIO.input(FLAME_DO)
        print("Sensor Output =", value)

        if value == 0:
            GPIO.output(ALERT, True)
            print("🔥 Flame Detected! ALERT ON")
        else:
            GPIO.output(ALERT, False)
            print("No flame detected. ALERT OFF")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()
