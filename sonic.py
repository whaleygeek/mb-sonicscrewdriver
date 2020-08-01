# sonic.py  05/04/2017  D.J.Whale - sonic screwdriver sound generator

import music
from microbit import *

def sonic(f=3000, fstep=32, fdepth=100, ton=10, toff=0, duration=2.0):
    try:
        ft = f
        music.pitch(ft)
        st = running_time()
        while running_time() < st+(duration*1000):
            sleep(ton)
            if toff != 0:
                music.stop()
                sleep(toff)
            fn = ft + fstep
            if fn >= f + fdepth or fn <= f - fdepth:
                fstep *= -1
            if fn != ft:
                ft = fn
                music.pitch(ft)
    finally:
        music.stop()
        
while True:
    if button_a.was_pressed():
        display.show(Image.SWORD)
        sonic(f=3000)
    elif button_b.was_pressed():
        display.show(Image.SWORD)
        sonic(f=4000)
    else:
        display.show(Image.DIAMOND)
        
