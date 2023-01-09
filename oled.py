"""
Initializes OLED display over I2C
"""

import board
import displayio
import adafruit_displayio_ssd1306

displayio.release_displays()

# i2c = board.I2C()  # uses board.SCL and board.SDA
i2c = board.STEMMA_I2C()  # Built-in STEMMA QT connector
display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)

def display(width: int, height: int):
    """
    Returns initialized display object
    """
    return adafruit_displayio_ssd1306.SSD1306(display_bus, width=width, height=height)
