from unicornhatmini import UnicornHATMini
from gpiozero import Button
from signal import pause
import time


unicornhatmini = UnicornHATMini()
unicornhatmini.set_brightness(1)
unicornhatmini.set_rotation(0)
width, height = unicornhatmini.get_shape()

button_b = Button(6)
button_y = Button(24)

def pomo():

    r = 255
    g = 0
    column = 15
    row = 6
    phase = "work"
    multiplier = 134

    while not(button_b.is_pressed):
        for x in range(16):
            for y in range(7):
                unicornhatmini.set_pixel(x,y,r,g,0)

                unicornhatmini.show()

        print("Running")
        
        while row > -1:
            while column > -1:
                for x in range(multiplier):
                    if not(button_b.is_pressed):
                        time.sleep(0.1)
                    else:
                        break
                unicornhatmini.set_pixel(column,row,0,0,0)
                unicornhatmini.show()
                column -= 1
            column = 15
            row -= 1
        row = 6

        if phase == "work":
            phase = "rest"
            multiplier = 27
            r = 0
            g = 255
        elif phase == "rest":
            phase = "work"
            multiplier = 134
            r = 255
            g = 0
        pass
    for x in range(16):
        for y in range(7):
            unicornhatmini.set_pixel(x,y,0,0,0)
unicornhatmini.show()

while True:
    while button_y.is_pressed:
        print("Button Y is pressed, starting.")
        pomo() 
