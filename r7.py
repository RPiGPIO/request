# PRACTICAL 7 - DHT11 TEMPERATURE AND HUMIDITY SENSOR
# File: practical_7_dht11.py

# =====================================
# PIN CONNECTIONS
# =====================================
# VCC  -> 3.3V -> Pin 1
# DATA -> GPIO4 -> Physical Pin 7
# GND  -> GND -> Pin 6

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect VCC to 3.3V
# 2. Connect DATA pin to GPIO4
# 3. Connect GND to Raspberry Pi GND
# 4. Run the code
# 5. Sensor values will print every 2 seconds

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Install:
# sudo apt install python3-pip
# pip3 install Adafruit_DHT

import Adafruit_DHT
import time

SENSOR = Adafruit_DHT.DHT11
PIN = 4

try:
    while True:
        humidity, temperature = Adafruit_DHT.read(SENSOR, PIN)

        if humidity is not None and temperature is not None:
            print("Temperature =", temperature, "°C")
            print("Humidity =", humidity, "%")
            print("------------------------")
        else:
            print("Sensor failure. Try again.")

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped")
