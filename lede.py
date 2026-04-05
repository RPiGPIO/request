# PRACTICAL 9 - 8x8 LED MATRIX MAX7219 (SIMPLIFIED)
# DIN -> GPIO10 -> Pin 19
# CS  -> GPIO8  -> Pin 24
# CLK -> GPIO11 -> Pin 23
# VCC -> 3.3V -> Pin 1
# GND -> Pin 6

# Enable SPI:
# sudo raspi-config
# Interface Options -> SPI -> Enable
# Install:
# pip3 install luma.led_matrix

import time
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT

# SPI setup
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

try:
    while True:
        # Diagonal line
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, i), fill="white")
        time.sleep(1)

        # Square border
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, 0), fill="white")
                draw.point((i, 7), fill="white")
                draw.point((0, i), fill="white")
                draw.point((7, i), fill="white")
        time.sleep(1)

        # Letter A
        with canvas(device) as draw:
            draw.text((1, 0), "A", fill="white")
        time.sleep(1)

        # Scrolling message
        show_message(
            device,
            "HELLO",
            fill="white",
            font=proportional(CP437_FONT),
            scroll_delay=0.1
        )

except KeyboardInterrupt:
    device.clear()
