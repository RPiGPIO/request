# PRACTICAL 9 - 8x8 LED MATRIX MAX7219
# File: practical_9_led_matrix.py

# =====================================
# PIN CONNECTIONS
# =====================================
# VCC  -> Pin 1  -> 3.3V
# GND  -> Pin 6  -> Ground
# DIN  -> Pin 19 -> MOSI GPIO10
# CS   -> Pin 24 -> CE0 GPIO8
# CLK  -> Pin 23 -> SCLK GPIO11

# =====================================
# HARDWARE / SETTINGS STEPS
# =====================================
# 1. Enable SPI
#    sudo raspi-config
#    Interface Options -> SPI -> Enable
# 2. Reboot Raspberry Pi
# 3. Install library:
#    pip3 install luma.led_matrix
# 4. Connect MAX7219 pins as above
# 5. Run the code

# PRACTICAL 9 - 8x8 LED MATRIX MAX7219
# DIN  -> GPIO10 -> Pin 19
# CS   -> GPIO8  -> Pin 24
# CLK  -> GPIO11 -> Pin 23
# VCC  -> 3.3V -> Pin 1
# GND  -> Pin 6

# Enable SPI:
# sudo raspi-config
# Interface Options -> SPI -> Enable
# Install:
# pip3 install luma.led_matrix

from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT
import time

# SPI setup
serial = spi(port=0, device=0, gpio=noop())

# Single 8x8 matrix
device = max7219(serial, cascaded=1, block_orientation=90, rotate=0)
device.contrast(50)

print("MAX7219 Matrix Ready...")

def blink_dot():
    with canvas(device) as draw:
        draw.point((3, 3), fill="white")
        draw.point((4, 3), fill="white")
        draw.point((3, 4), fill="white")
        draw.point((4, 4), fill="white")

def diagonal_line():
    with canvas(device) as draw:
        for i in range(8):
            draw.point((i, i), fill="white")

def border_box():
    with canvas(device) as draw:
        for x in range(8):
            draw.point((x, 0), fill="white")
            draw.point((x, 7), fill="white")
        for y in range(8):
            draw.point((0, y), fill="white")
            draw.point((7, y), fill="white")

def show_letter_A():
    with canvas(device) as draw:
        points = [
            (1,7),(1,6),(1,5),(1,4),(1,3),(1,2),(1,1),
            (2,0),(3,0),(4,0),(5,0),
            (6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(6,7),
            (2,4),(3,4),(4,4),(5,4)
        ]
        for p in points:
            draw.point(p, fill="white")

try:
    while True:
        device.clear()
        blink_dot()
        time.sleep(1)

        device.clear()
        diagonal_line()
        time.sleep(1)

        device.clear()
        border_box()
        time.sleep(1)

        device.clear()
        show_letter_A()
        time.sleep(2)

        device.clear()
        show_message(
            device,
            "IOT",
            fill="white",
            font=proportional(CP437_FONT),
            scroll_delay=0.1
        )
        time.sleep(1)

except KeyboardInterrupt:
    device.clear()
    print("Stopped")
