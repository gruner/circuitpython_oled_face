"""
Animates a face on OLED display using bmp images
"""

import displayio
import time
from oled import display

# Initialize the OLED display
display = display(width=128, height=64)
display.auto_brightness = False
display.brightness = 0

# Face image names
SLEEPING = "sleeping"
SLEEPING_EYES = "sleeping_eyes"
SLEEPY = "sleepy"
SLEEPY_BLINK = "sleepy_blink"
SQUEE = "squee"
STANDARD = "standard"
TEARS = "tears"
UPSET = "upset"
UPSET_SQUINT = "upset_squint"
WINK = "wink"

# Create a dict for face groups
face_images = {}


def load_face_images():
    """
    Loades face image files and creates a displayio object ready for display
    """
    img_names = [
        SLEEPING,
        SLEEPING_EYES,
        SLEEPY,
        SLEEPY_BLINK,
        SQUEE,
        STANDARD,
        TEARS,
        UPSET,
        UPSET_SQUINT,
        WINK
    ]
    for name in img_names:
        # Create a Bitmap object from the file
        # TODO: validate file path
        face = displayio.OnDiskBitmap("img/{}.bmp".format(name))
        tile_grid = displayio.TileGrid(face, pixel_shader=face.pixel_shader)
        group = displayio.Group()
        group.append(tile_grid)
        face_images[name] = group


def show_face(face, duration):
    """
    Displays one of the preloaded faces for the supplied duration
    """
    display.show(face_images[face])
    time.sleep(duration)


def face_sleeping():
    """
    Animates sleeping face
    """
    for _ in range(3):
        show_face(SLEEPING, .5)
        show_face(SLEEPING_EYES, .5)


def face_awake_from_sleep():
    """
    Animates face awaking from sleep
    """
    for _ in range(3):
        show_face(SLEEPY, .5)
        show_face(SLEEPY_BLINK, 0.25)
    show_face(SLEEPY, .5)


def face_standard():
    """
    Animates standard face
    """
    for _ in range(3):
        show_face(STANDARD, 3)
        show_face(SQUEE, 0.5)
        show_face(STANDARD, 3)
        show_face(WINK, 0.5)
    face_awake_from_sleep()

load_face_images()

display.show(face_images[SLEEPING])

# Fade up the backlight
for i in range(100):
    display.brightness = 0.01 * i
    time.sleep(0.05)

face_awake_from_sleep()

while True:
    face_standard()
