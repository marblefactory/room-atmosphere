import RPi.GPIO as GPIO


box_alarm_pin = 21


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(box_alarm_pin, GPIO.OUT)



def raise_alarm():
    """
    Turns the alarm on.
    """
    GPIO.output(box_alarm_pin, GPIO.HIGH)
    
    
def lower_alarm():
    """
    Turns the alarm off.
    """
    GPIO.output(box_alarm_pin, GPIO.LOW)
    
