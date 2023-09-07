import time

# Scale time by markiplier. Set this to 1 for a clock alligned with reality
class scale_time_provider:

    initial_time = time.time()

    def __init__(self, markiplier):
        self.markiplier = markiplier

    def get_time(self):
        return (time.time() - self.initial_time)*self.markiplier + self.initial_time

# Class for the state of a clock
class Clock:

    offset = 0
    alarm = False
    alarm_offset = 0

    def __init__(self, time_provider):
        self.time_provider = time_provider

    # Return the time of day in seconds (0-83399)
    def get_time(self):
        return (self.time_provider.get_time() + self.offset) % 86400

    # Change the clock's offset relative to the time provider
    # If the input is 0, get_time() will initially return 12:00 AM
    def set_time(self, offset):

        # Change the offset
        self.offset = offset - self.time_provider.get_time() % 86400

    def get_alarm_time(self):
        return self.alarm_offset % 86400

    # Set the offset for the alarm
    def set_alarm(self, alarm_time):
        self.alarm_offset = alarm_time % 86400

    

# from display import format_time
# import math
# scale = scale_time_provider(30)
# main_clock = Clock(scale)
# run = True

# offset = 0
# main_clock.set_time(offset)

# while run:

#     display_time = format_time(math.floor(main_clock.get_time()))
#     print(display_time)

#     if (display_time == ("1210", True)):
#         print("Alarm")

#     time.sleep(0.05)