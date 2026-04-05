# PRACTICAL 4 - TELEGRAM LED CONTROL
# File: practical_4_telegram_led.py

# =====================================
# PIN CONNECTIONS
# =====================================
# Red LED    -> GPIO22 -> Physical Pin 15
# Yellow LED -> GPIO23 -> Physical Pin 16
# Both GND   -> Pin 6 / 9

# =====================================
# HARDWARE STEPS
# =====================================
# 1. Connect Red LED to GPIO22 using resistor
# 2. Connect Yellow LED to GPIO23 using resistor
# 3. Connect both negatives to GND
# 4. Create Telegram bot using BotFather
# 5. Copy bot token and paste below
# 6. Run python file
# 7. Send commands from Telegram app

# =====================================
# LIBRARY / SETTINGS
# =====================================
# Install:
# sudo apt install python3-pip
# pip3 install telepot

import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 22
YELLOW = 23

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(YELLOW, GPIO.OUT)

# Paste your Telegram bot token here
TOKEN = "YOUR_BOT_TOKEN"

def control_led(msg):
    command = msg['text'].lower()

    if command == "red on":
        GPIO.output(RED, GPIO.HIGH)

    elif command == "red off":
        GPIO.output(RED, GPIO.LOW)

    elif command == "yellow on":
        GPIO.output(YELLOW, GPIO.HIGH)

    elif command == "yellow off":
        GPIO.output(YELLOW, GPIO.LOW)

    elif command == "all on":
        GPIO.output(RED, GPIO.HIGH)
        GPIO.output(YELLOW, GPIO.HIGH)

    elif command == "all off":
        GPIO.output(RED, GPIO.LOW)
        GPIO.output(YELLOW, GPIO.LOW)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, control_led).run_as_thread()

print("Telegram bot started...")

while True:
    time.sleep(10)
