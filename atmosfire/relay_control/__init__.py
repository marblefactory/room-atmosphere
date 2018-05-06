import RPi.GPIO as GPIO


def raise_alarm():
    """
    Turns the alarm on.
    """
    pass



def lower_alarm():
    """
    Turns the alarm off.
    """
    GPIO.output(box_alarm_pin, GPIO.LOW)
