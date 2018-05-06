import time
from atmosfire import relay_control


if __name__ == '__main__':


    relay_control.setup()

    time.sleep(1)
    relay_control.raise_alarm()
    
    time.sleep(5)
    relay_control.lower_alarm()


