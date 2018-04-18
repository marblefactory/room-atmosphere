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

    fixed(ser, 1, 'FF0000')
    # breathing(ser, args.gui, args.channel, args.colors, args.speed)
    # elif args.command == 'fading':
    #     fading(ser, args.gui, args.channel, args.colors, args.speed)
    # elif args.command == 'marquee':
    #     marquee(ser, args.gui, args.channel, args.color, args.speed, args.size, args.backwards)
    # elif args.command == 'cover_marquee':
    #     cover_marquee(ser, args.gui, args.channel, args.colors, args.speed, args.backwards)
    # elif args.command == 'pulse':
    #     pulse(ser, args.gui, args.channel, args.colors, args.speed)
    # elif args.command == 'spectrum':
    #     spectrum(ser, args.channel, args.speed, args.backwards)
    # elif args.command == 'alternating':
    #     alternating(ser, args.gui, args.channel, args.colors, args.speed, args.size, args.moving, args.backwards)
    # elif args.command == 'candlelight':
    #     candlelight(ser, args.gui, args.channel, args.color)
    # elif args.command == 'wings':
    #     wings(ser, args.gui, args.channel, args.color, args.speed)
    # elif args.command == 'audio_level':
    #     audio_level(ser, args.gui, args.channel, args.colors, args.tolerance, args.refresh)
    # elif args.command == 'custom':
    #     custom(ser, args.gui, args.channel, args.colors, args.mode, args.speed)
    # elif args.command == 'power':
    #     power(ser, args.channel, args.state)
    # elif args.command == 'unitled':
    #     unitled(ser, args.state)
    # elif args.command == 'profile':
    #     if args.profile_command == 'add':
    #         profile_add(args.name)
    #     elif args.profile_command == 'rm':
    #         profile_rm(args.name)
    #     elif args.profile_command == 'apply':
    #         profile_apply(ser, args.name)
    #     elif args.profile_command == 'list':
    #         profile_list()
    #     else:
    #         raise InvalidCommand("No such profile command")
    # else:
    #     raise InvalidCommand("No such mode")



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
    # outputs = previous.get_colors(channel, command)
    write(ser, command)


# def breathing(ser, gui, channel, color, speed):
#
#     if 1 <= gui <= 8:
#         color = []
#         for i in range(gui):
#             color.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     command = create_command(ser, channel, color, "breathing", 0, 0, 0, speed)
#
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def fading(ser, gui, channel, color, speed):
#
#     if 1 <= gui <= 8:
#         color = []
#         for i in range(gui):
#             color.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     command = create_command(ser, channel, color, "fading", 0, 0, 0, speed)
#
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def marquee(ser, gui, channel, color, speed, size, direction):
#
#     if gui != 0:
#         gui = 1
#         for i in range(1):
#             color = picker.pick("Color "+str(i+1) + " of "+str(gui))
#
#     command = create_command(ser, channel, [color], "marquee", direction, 0, size, speed)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def cover_marquee(ser, gui, channel, color, speed, direction):
#
#     if 1 <= gui <= 8:
#         color = []
#         for i in range(gui):
#             color.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     command = create_command(ser, channel, color, "cover_marquee", direction, 0, 0, speed)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def pulse(ser, gui, channel, color, speed):
#
#     if 1 <= gui <= 8:
#         color = []
#         for i in range(gui):
#             color.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     command = create_command(ser, channel, color, "pulse", 0, 0, 0, speed)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def spectrum(ser, channel, speed, direction):
#
#     command = create_command(ser, channel, ["0000FF"], "spectrum", direction, 0, 0, speed)
#
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def alternating(ser, gui, channel, color, speed, size, moving, direction):
#
#     if gui != 0:
#         color = []
#         gui = 2
#         for i in range(2):
#             color.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     if moving:
#         option = 1
#     else:
#         option = 0
#
#     command = create_command(ser, channel, color, "alternating", direction, option, size, speed)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def candlelight(ser, gui, channel, color):
#
#     if gui != 0:
#         color = picker.pick("Color")
#
#     command = create_command(ser, channel, [color], "candlelight", 0, 0, 0, 0)
#
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def wings(ser, gui, channel, color, speed):
#
#     if gui != 0:
#         color = picker.pick("Color")
#
#     command = create_command(ser, channel, [color], "wings", 0, 0, 0, speed)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
#
# def power(ser, channel, state):
#     if state.lower() == 'on':
#         fixed(ser, 0, channel, "FFFFFF")
#     elif state.lower() == 'off':
#         fixed(ser, 0, channel, "000000")
#     else:
#         raise InvalidCommand("No such power state")
#
# def unitled(ser, state):
#     outputs = [70, 0, 192, 0, 0, 0, 0]
#     if state.lower() == 'on':
#         outputs[6] = 255
#     elif state.lower() == 'off':
#         outputs[5] = 255
#     else:
#         raise InvalidCommand("No such unit led state")
#     ser.write(bytearray(outputs))
#     ser.read()
#
# def custom(ser, gui, channel, colors, mode, speed):
#     strips = [strips_info(ser, 1), strips_info(ser, 2)]
#
#     if mode not in ['fixed', 'breathing', 'wave']:
#         raise InvalidCommand("No such mode for custom")
#
#     if 1 <= gui <= 40:
#         colors = []
#         for i in range(gui):
#             colors.append(picker.pick("Color "+str(i+1) + " of "+str(gui)))
#
#     command = create_custom(ser, channel, colors, mode, 0, 0, 0, speed, strips)
#     outputs = previous.get_colors(channel, command)
#     write(ser, outputs)
#
# def animated(ser, channel, colors, speed):
#     if not inspect.isclass(ser):
#         ser = serial.Serial(ser, 256000)
#     strips = [strips_info(ser, 1), strips_info(ser, 2)]
#     init(ser)
#     while True:
#         for round in colors:
#             command = create_custom(ser, channel, round, "audio", 0, 0, 0, 0, strips)
#             outputs = previous.get_colors(channel, command)
#             write(ser, outputs)
#             sleep(speed / 1000.0)
#
#
# def profile_add(name):
#     previous.add_profile(name)
#
# def profile_rm(name):
#     previous.rm_profile(name)
#
# def profile_apply(ser, name):
#     commands = previous.apply_profile(name)
#     if type(commands) is dict:
#         return commands
#     init(ser)
#     write(ser, commands)
#     return None
#
# def write_previous(ser):
#     write(ser, previous.get_previous())

if __name__ == '__main__':
    main()
