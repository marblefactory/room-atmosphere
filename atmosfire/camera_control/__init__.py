def setup(arduino):
    arduino.set_pin_mode(0, 'I')
    arduino.set_pin_mode(1, 'I')
    arduino.set_pin_mode(2, 'I')
    arduino.digital_write(2 ,1)

def pan_vector(arduino):
    x_offset = 523
    y_offset = 503

    x_pin    = 0
    y_pin    = 1
    s_pin    = 2

    x = 1#int(arduino.analog_read(x_pin) - x_offset)
    y = 1# int(arduino.analog_read(y_pin) - y_offset)
    s = int(arduino.digital_read(s_pin))


    return x, y, s
        
    
