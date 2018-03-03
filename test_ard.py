import time
from atmosfire import Arduino, camera_control


if __name__ == '__main__':
    
    a = Arduino()    
    time.sleep(3)

    camera_control.setup(a)

    for i in range(10):

        x, y, s = camera_control.pan_vector(a)
#        print("X:", x)
#        print("Y:", y)
        print("S:", s)

        time.sleep(1)



    a.close()
