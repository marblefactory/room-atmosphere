import numpy as np
import math

def setup(arduino):
    pass


def pan_vector(arduino):
    x_offset = 523
    y_offset = 503

    x_pin    = 0
    y_pin    = 1

    x = int(arduino.analog_read(x_pin) - x_offset)
    y = int(arduino.analog_read(y_pin) - y_offset)

    r = int(np.hypot(y,x))
    if (r<10):
        return 0, 0
    else:
        return r, int(math.degrees(np.arctan2(y,x)))

def zoom_level(arduino):
    pin = 2
    return int(arduino.analog_read(pin))
