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

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from time import sleep

# SPI setup
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

try:
    while True:
        # Diagonal line pattern
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, i), fill="white")
        sleep(2)

        # Square border pattern
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 0), fill="white")
                draw.point((i, 7), fill="white")
                draw.point((0, i), fill="white")
                draw.point((7, i), fill="white")
        sleep(2)

        device.clear()

except KeyboardInterrupt:
    device.clear()
