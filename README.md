# MetalGearClock
Code for the project's clock and user display. Run main.py to start the clock.

The game Metal Gear Solid has an in-game timer countdown for certain game events. We wanted to turn that game timer into a functioning alarm clock. There was no help for this online, so we made it from scratch. In this repository is the code and all necessary files
for the software part of the project.

![image](https://github.com/chris-derman03/MetalGearClock/assets/129346834/0811d432-3ef9-4b34-a6f3-86e6e6d186aa)

![image](https://github.com/chris-derman03/MetalGearClock/assets/129346834/354d5d5d-2dd9-4b5d-aa95-381ca7b3d979)

The clock starts with an animation. It enters the time-setting phase, in which the user can use any of the 6 triangle buttons to change the clock's time. Or, the user could press the clock logo to exit the time-changing phase and set the clock
time to whatever they desired. To re-enter this phase, simply press the clock button again.
The alarm-setting phase follows very similarly, but is initiated instead with the bell icon. This will look and work similar to the time-changing/time-setting phase, but instead does not modify the actual time, but just sets an alarm. Again, to exit
press the bell icon again.
To actually turn the alarm on, the user must press the toggle alarm button just next to the time-setting phase button (clock icon).
Once the alarm goes off, the only way to turn it off is to press this toggle again.
Alternatively, the user may press spacebar to snooze for 5 minutes.

(The inputs, which are just left clicks and space bar presses, are temporary and are subject to change depending on how you want to implement the physical aspect of the project.)

![image](https://github.com/user-attachments/assets/b339376b-4760-4d3e-8a5c-0f2264ef08df)




CLOCK FUNCTION:
The clock's internal time is just the CPU's internal clock. Any time the user changes the time, they are changing the offset from that CPU time.
If the CPU time is 6:00 AM UTC, and the user wants the clock to show 8:23 AM, they can change the time easily, and the clock will show 8:23 AM. In the background, the clock class' offset attribute
is 8580, which is two hours and twenty three minutes in seconds.
