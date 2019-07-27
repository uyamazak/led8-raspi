import RPi.GPIO as GPIO
from gpiozero import LED

PIN_NUMS_DICT = {1:4, 2:17, 3:27, 4:22,
                 5:18, 6:23, 7:24, 8:25} 

def init_leds():
    leds = {}
    for key, val in PIN_NUMS_DICT.items():
        leds[key] = LED(val)
    return leds


def update_pattern(leds, on_keys):
    for key, val in leds.items():
        if key in on_keys:
            leds[key].on()
        else:
            leds[key].off()
