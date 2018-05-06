import serial
import time




# # Exceptions
# class InvalidCommand(Exception):
#     pass
#
# class InvalidUser(Exception):
#     pass

def main():
    #if os.geteuid() != 0:
    #    sys.exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'.")



    ser = serial.Serial("/dev/ttyACM0", 256000)

    fixed(ser, 0, 'FF0000')

def strips_info(ser, channel):
    time.sleep(0.2)
    out = bytearray.fromhex("8D0" + str(channel))
    ser.write(out)
    time.sleep(1)
    out = ser.read(ser.in_waiting).hex()
    if out:
        r = int(out[-1])
    else:
        r = -1
    if r <= 0:
        r = 1
    return r


def create_command(ser, channel, colors, mode, direction, option, group, speed):
    init(ser)

    commands = []
    channel_commands = []
    modes = {
        "fixed": 0,
        "breathing": 7,
        "fading": 1,
        "marquee": 3,
        "cover_marquee": 4,
        "pulse": 6,
        "spectrum": 2,
        "alternating": 5,
        "candlelight": 9,
        "wings": 12,
        "wave": 13,
        "alert": 8
    }

    strips = [0, strips_info(ser, 1)-1, strips_info(ser, 2)-1]
    strips[0] = max(strips)

    if channel == 0:
        channels = [1, 2]
    else:
        channels = [channel]

    for channela in channels:
        commands = []
        for i, color in enumerate(colors):
            command = []
            command.append(75)
            command.append(channela)
            command.append(modes[mode])
            command.append(direction << 4 | option << 3 | strips[channela])
            command.append(i << 5 | group << 3 | speed)
            for z in range(40):
                command.append(int(color[2:4], 16))
                command.append(int(color[:2], 16))
                command.append(int(color[4:], 16))
            command = bytearray(command)
            commands.append(command)

        channel_commands.append(commands)
    return channel_commands

def init(ser):
    #C0(ser)
    # Took out bytearray([70, 0, 192, 0, 0, 0, 255])
    initial = [bytearray.fromhex("4B" + "00"*124)]
    for array in initial:
        ser.write(array)
        time.sleep(0.2)
        ser.read(ser.in_waiting)
def write(ser, outputs):
    for channel in outputs:
        for line in channel:
            if line:
                ser.write(line)
                ser.read()


def fixed(ser, channel, color):

    command = create_command(ser, channel, [color], "fixed", 0, 0, 0, 2)
    # outputs = previous.get_colors(channel, command[0])
    write(ser, command)


if __name__ == '__main__':
    main()
