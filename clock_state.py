import time

# For this file, please read "markiplier" as multiplier

# Our clock class needs a time provider, for a clock in line with reality it should just be one with a markiplier of 1
# If you want the clock to move at 1 minute per IRL second, set the markiplier to 60 (don't quote me on that I didn't do the math but it seems to work like that)
class scale_time_provider:

    initial_time = time.time()

    def __init__(self, markiplier):
        self.markiplier = markiplier

    # If the markiplier is 1, then this method is equivalent to time.time(),
    # which makes sense because a markiplier of 1 shouldn't affect the clock's counting rate
    def get_time(self):
        return (time.time() - self.initial_time)*self.markiplier + self.initial_time

# Class for the state of a clock
class Clock:

    offset = 0
    alarm_offset = 0

    def __init__(self, time_provider):
        self.time_provider = time_provider

    # Return the time of day in seconds (0-83399) of the clock (the user set this time)
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
