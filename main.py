import pygame
pygame.init()
import time
import copy
import math

from clock_state import Clock, scale_time_provider
from display import format_time
from button import ButtonManager








#=============================================
# Window Stuff
#=============================================

SCREEN_WIDTH=970
SCREEN_HEIGHT=780
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alarm Clock")

DEFAULT_ALLOWED_EVENTS = [pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]

pygame.event.set_blocked(None) # Block all events
pygame.event.set_allowed(DEFAULT_ALLOWED_EVENTS) # Allow default-state events














#=============================================
# Background Images
#=============================================

EVASION = 0
ALERT = 1
JAMMING = 2

# Load frames of the evasion animation
EVASION_ANIMATION = []
for _ in range(8):
    i = _ + 1
    EVASION_ANIMATION += [pygame.image.load("resources/img/evasion_frames/evasion_" + str(i) + ".jpg")]

# Load frames of the alert animation
ALERT_ANIMATION = []
for _ in range(8):
    i = _ + 1
    ALERT_ANIMATION += [pygame.image.load("resources/img/alert_frames/alert_" + str(i) + ".jpg")]

# Load frames of the jamming animation
JAMMING_ANIMATION = []
for _ in range(50):
    JAMMING_ANIMATION += [pygame.image.load("resources/img/jamming_frames/frame_" + str(_).rjust(3, "0") + ".jpg")]


# Set the background to the given background, codes are above
# Calculates which frame to draw based on the clock time
def set_background(time, animation_frames, animation_duration=0.8):

        time /= animation_duration/len(animation_frames)
        idx = math.floor(time) % len(animation_frames)
        screen.blit(animation_frames[idx], (0,0))

























#=============================================
# Display Functions
#=============================================

# Font and font size for display text
time_font = pygame.font.Font("resources/clock_font.otf", 149) # Font for the actual time display
ampm_font = pygame.font.Font("resources/clock_font.otf", 80) # Same as above, but for am and pm text

# Locations to render time digits
LOCATIONS = [(135,473),(300,473),(535,473),(700,473)]

# Takes in # of seconds between 0 and 83499
# Formats those seconds (i.e., 12:32 AM    --->     ("1232", True))
def draw_text(time, color="Black"):

    time_data = format_time(math.floor(time))

    time = time_data[0]
    am = time_data[1]
    
    # Split the 4 digit string into a list of digits
    digits = [*time]

    # In the case where the first digit is empty, manually insert "" as an element
    if len(digits) < 4:
        digits = [""] + digits

    img = None

    # Render each digit
    for i in range(len(digits)):
        # if (digits[i] != ""):
        img = time_font.render(digits[i], False, color)
        screen.blit(img,LOCATIONS[i])

    # blit (draw) AM or PM at the manually discovered pixel location
    if (am):
        am_text = ampm_font.render("A M", True, color)
        screen.blit(am_text, (650,275))
    else:
        pm_text = ampm_font.render("P M", True, color)
        screen.blit(pm_text, (650,275))












#=============================================
# Sounds
#=============================================

alarm_sound = pygame.mixer.music.load("resources/sound_effects/alarm.wav")









#=============================================
# Buttons
#=============================================

buttonManager = ButtonManager()

# Load clock image and scale it down
clock = pygame.image.load("resources/img/clock.png").convert_alpha()
clock = pygame.transform.scale(clock, (80,86))

# Load Bell image and scale it down
bell = pygame.image.load("resources/img/bell.png").convert_alpha()
bell = pygame.transform.scale(bell, (80,86))

# Create Phase changing button
changeTime = buttonManager.add_button(540,220, copy.copy(clock)) # i.e., clicking this button enters the time changing phase
setAlarm = buttonManager.add_button(540,320, copy.copy(bell))



# Load images for the alarm toggle buttons
alarm_on_img = pygame.image.load("resources/img/alarm_on.png").convert_alpha()
alarm_on_img = pygame.transform.scale(alarm_on_img, (164, 85))
alarm_off_img = pygame.image.load("resources/img/alarm_off.png").convert_alpha()
alarm_off_img = pygame.transform.scale(alarm_off_img, (164, 85))

# Create alarm toggle buttons
alarmOn = buttonManager.add_button(668,230,copy.copy(alarm_on_img))
alarmOff = buttonManager.add_button(668,230,copy.copy(alarm_off_img))



# Load triangle image and scale it down
triangle = pygame.image.load("resources/img/triangle.png").convert_alpha()
triangle = pygame.transform.scale(triangle, (115,76))

# Make another image instance for the triangle facing upwards
triangleUp = pygame.transform.rotate(triangle, 180)

# Create the 4 button instances for changing the time
hourUp = buttonManager.add_button(10, 500, copy.copy(triangleUp))
hourDown = buttonManager.add_button(7, 600, copy.copy(triangle))
minuteUp = buttonManager.add_button(850, 500, copy.copy(triangleUp))
minuteDown = buttonManager.add_button(847, 600, copy.copy(triangle))
minuteUpLarge = buttonManager.add_button(850, 425, copy.copy(triangleUp))
minuteDownLarge = buttonManager.add_button(847, 675, copy.copy(triangle))






















#=============================================
# Program Loop
#=============================================

scale = scale_time_provider(1)
main_clock = Clock(scale)
main_clock.set_time(0)
main_clock.set_alarm(0)

# Whether to run the main loop
run = True

# Booleans for what phase we are in
change_time = True
set_alarm = False
alarm_phase = False

# Toggle for the alarm
alarm = False

# If snoozed, when to redo the alarm
snooze_alarm_time = -1

# Initial offset and animation start anchor
offset = 0
animation_start = main_clock.get_time()

# Startup animation
while main_clock.get_time() - animation_start <= 5:

    set_background(main_clock.get_time(), JAMMING_ANIMATION, 5)
    pygame.display.update()

    time.sleep(0.05)

while run:

    buttonManager.reset()

    # Time changing phase or set_alarm
    if (change_time or set_alarm):

        # Clear screen
        set_background(main_clock.get_time(), EVASION_ANIMATION)
        
        # Get the current clock time
        current_time = main_clock.get_time()

        # Text flashing animation
        if (current_time - animation_start) % 1 > 0.25:

            # Draw the time
            draw_text(offset)

        # Which exit button to draw
        if (change_time):    
            # Draw exit button
            changeTime.draw(screen)
        else:
            setAlarm.draw(screen)

        # Draw the time changing buttons
        hourUp.draw(screen)
        hourDown.draw(screen)
        minuteUp.draw(screen)
        minuteDown.draw(screen)
        minuteUpLarge.draw(screen)
        minuteDownLarge.draw(screen)

    # Alarm phase
    elif (alarm_phase):

        # Set screen to alarm background
        set_background(main_clock.get_time(), ALERT_ANIMATION)

        # Render new time
        draw_text(main_clock.get_time())

        # Draw the alarm toggle button
        if (alarm):
            alarmOn.draw(screen)
        else:
            alarmOff.draw(screen)

    # Default phase (time counting)
    else:
        
        # Clear the screen and add all buttons
        set_background(main_clock.get_time(), EVASION_ANIMATION)
        changeTime.draw(screen)
        setAlarm.draw(screen)

        # Render new time
        draw_text(main_clock.get_time())

        # Draw the alarm toggle button
        if (alarm):
            alarmOn.draw(screen)
        else:
            alarmOff.draw(screen)

        # If alarm is on, check if we should set off the alarm
        if (alarm):
            # If the time is equal to the alarm, toggle the alarm phase
            if (main_clock.get_time() // 60 == main_clock.get_alarm_time() // 60):
                # Only set off the alarm if we haven't snoozed it
                if (snooze_alarm_time == -1):
                    alarm_phase = True
                    pygame.mixer.music.play(-1) # play alarm sound infinitely

            # If the clock was snoozed, check the new snooze time
            if (snooze_alarm_time != -1):
                if (main_clock.get_time() // 60 == snooze_alarm_time):
                    alarm_phase = True
                    pygame.mixer.music.play(-1) # play alarm sound infinitely
                    snooze_alarm_time = -1 # Reset the snooze
    
    # Event Handler
    for event in pygame.event.get():

        # If red X is clicked, exit the game
        if (event.type == pygame.QUIT):
            run = False
            pygame.quit()

        # Spacebar is our snooze button
        elif (event.type == pygame.KEYDOWN):
            if (event.key == pygame.K_SPACE):
                
                # Only snooze if we are in the alarm phase
                if (alarm_phase):

                    # Exit the alarm phase
                    alarm_phase = False
                    pygame.mixer.music.stop()

                    # Set a new alarm-time to 5 minutes in the future
                    # We don't directly change the alarm time
                    snooze_alarm_time = main_clock.get_time() // 60 + 5

        # If the user clicks
        elif (event.type == pygame.MOUSEBUTTONDOWN):

            # get cursor position
            pos = event.pos

            # If the cursor was over the changeTime button
            if (changeTime.is_clicked(pos)):

                # TIME CHANGING PHASE
                change_time = not change_time

                # If we are enterting the time-changing phase
                if (change_time):
                    offset = main_clock.get_time() // 60 * 60
                    animation_start = main_clock.get_time()
                # If we are exiting the time-changing phase
                else:
                    main_clock.set_time(offset)

            # If the cursor was over the setAlarm button
            elif (setAlarm.is_clicked(pos)):

                # SETTING ALARM PHASE
                set_alarm = not set_alarm

                # If we are enterting the setting alarm phase
                if (set_alarm):
                    offset = main_clock.get_alarm_time() // 60 * 60
                    animation_start = main_clock.get_time()
                # If we are exiting the setting alarm phase
                else:
                    main_clock.set_alarm(offset)

            # If the cursor was over the alarm toggle button
            elif (alarmOn.is_clicked(pos)):
                # The alarm off toggle should also exit the alarm phase
                alarm_phase = False
                alarm = False
                pygame.mixer.music.stop()
            elif (alarmOff.is_clicked(pos)):
                alarm = True

            # If the cursor was over any of the time-chaning buttons
            elif (hourUp.is_clicked(pos)):
                offset = (offset + 3600) % 86400
            elif (hourDown.is_clicked(pos)):
                offset =  (offset - 3600) % 86400
            elif (minuteUp.is_clicked(pos)):
                offset = (offset + 60) % 86400
            elif (minuteDown.is_clicked(pos)):
                offset = (offset - 60) % 86400
            elif (minuteUpLarge.is_clicked(pos)):
                offset = (offset + 600) % 86400
            elif (minuteDownLarge.is_clicked(pos)):
                offset = (offset - 600) % 86400

    pygame.display.update()

    # 20 Ticks per second
    time.sleep(0.05)

# Safety-net quit
pygame.quit()