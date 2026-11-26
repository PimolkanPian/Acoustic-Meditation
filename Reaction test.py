from machine import Pin
import utime
import random
import uos

# ====== Create logs folder ======
FOLDER = "button2026"
try:
    uos.mkdir(FOLDER)
except OSError:
    pass  # already exists

# ====== Generate timestamped filename ======
t = utime.localtime()
ts = "{}{:02d}{:02d}_{:02d}{:02d}{:02d}".format(t[0], t[1], t[2], t[3], t[4], t[5])
filename = "{}/ButtonGameTest_{}.csv".format(FOLDER, ts)

# LEDs
led1 = Pin(6, Pin.OUT) #red
led2 = Pin(7, Pin.OUT) #green

# Buttons (pull-up enabled, so pressed = 0)
button1 = Pin(27, Pin.IN, Pin.PULL_UP)
button2 = Pin(26, Pin.IN, Pin.PULL_UP)

# Open CSV file for writing
with open(filename, "w") as f:
    # Write header
    f.write("Round,Button,Press_Time_ms,Reaction_Time_ms\n")

    # Run for 5 rounds
    for round_num in range(1, 6):
        print("Round", round_num)

        # Turn both LEDs off first
        led1.value(0)
        led2.value(0)

        # Randomly choose LED1 or LED2
        choice = random.choice([1, 2])
        if choice == 1:
            led1.value(1)
            #print("Press Button1")
        else:
            led2.value(1)
            #print("Press Button2")

        # Record the time when LED turned on
        start_time = utime.ticks_ms()

        # Wait for correct button press
        while True:
            if choice == 1 and button1.value() == 0:
                press_time = utime.ticks_ms()
                reaction_time = utime.ticks_diff(press_time, start_time)
                #print("Button1 pressed at", press_time, "ms (Reaction:", reaction_time, "ms)")
                f.write("{},{},{},{}\n".format(round_num, "red", press_time, reaction_time)) #1
                break
            elif choice == 2 and button2.value() == 0:
                press_time = utime.ticks_ms()
                reaction_time = utime.ticks_diff(press_time, start_time)
                #print("Button2 pressed at", press_time, "ms (Reaction:", reaction_time, "ms)")
                f.write("{},{},{},{}\n".format(round_num, "green", press_time, reaction_time)) #2
                break
            utime.sleep(0.0001)  # debounce

        # Turn off LEDs and pause before next round
        led1.value(0)
        led2.value(0)
        utime.sleep(0.5)

print("Completed!")







