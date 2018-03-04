import time
from atmosfire import Arduino, camera_control, relay_control


if __name__ == '__main__':

    a = Arduino()
    time.sleep(3)

    camera_control.setup(a)
    relay_control.setup(a)

    time.sleep(3)

    relay_control.raise_alarm(a)

    for i in range(20):

        r, t = camera_control.pan_vector(a)
        z    = camera_control.zoom_level(a)
        print("R:", r)
        print("T:", t)
        print("Z:", z)

        print("\n")

        time.sleep(0.5)



    a.close()
