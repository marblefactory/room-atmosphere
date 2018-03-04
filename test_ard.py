import time
from atmosfire import Arduino, camera_control


if __name__ == '__main__':

    a = Arduino()
    time.sleep(3)

    camera_control.setup(a)

    for i in range(20):

        r, t = camera_control.pan_vector(a)
        print("R:", r)
        print("T:", t)

        time.sleep(0.5)



    a.close()
