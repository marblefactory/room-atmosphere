from threading import Thread
import time

def setup(arduino):
    arduino.set_pin_mode(2, 'O')
    time.sleep(1)
    arduino.digital_write(2, 1)

def _async_alarm(arduino=None, length=5):
    arduino.digital_write(2,0)
    time.sleep(length)
    arduino.digital_write(2,1)


def raise_alarm(arduino):
    thread = Thread(target = _async_alarm, kwargs={'arduino':arduino, 'length':5})
    thread.start()
