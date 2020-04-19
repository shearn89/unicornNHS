#!/usr/bin/env python

import time 
import math
import sys

import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(90)
unicorn.brightness(0.5)
width,height=unicorn.get_shape()


print("Reticulating splines")

dark = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

letter_n = [
        [ white, dark, dark, dark, dark, dark, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, white, dark, dark, dark, white, white ],
        [ white, white, white, white, dark, dark, white, white ],
        [ white, white, dark, white, white, dark, white, white ],
        [ white, white, dark, dark, white, white, white, white ],
        [ white, white, dark, dark, dark, white, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
    ]

letter_h = [
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, white, white, white, white, white, white ],
        [ white, white, white, white, white, white, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
        [ white, white, dark, dark, dark, dark, white, white ],
    ]

letter_s = [
        [ dark, white, white, white, white, white, white, dark ],
        [ white, white, white, white, white, white, white, white ],
        [ white, white, dark, dark, dark, dark, dark, dark ],
        [ white, white, white, white, white, white, white, dark ],
        [ dark, white, white, white, white, white, white, white ],
        [ dark, dark, dark, dark, dark, dark, white, white ],
        [ white, white, white, white, white, white, white, white ],
        [ dark, white, white, white, white, white, white, dark ],
    ]

def show_matrix(matrix):
    delay=0.5
    unicorn.set_pixels(matrix)
    unicorn.show()
    time.sleep(delay)


def nhs():
    show_matrix(letter_n)
    show_matrix(letter_h)
    show_matrix(letter_s)

def rainbow(loops):
    i = 0.0
    offset = 30
    for i in range(loops):
            i = i + 0.3
            for y in range(height):
                    for x in range(width):
                            r = (math.cos((x+i)/2.0) + math.cos((y+i)/2.0)) * 64.0 + 128.0
                            g = (math.sin((x+i)/1.5) + math.sin((y+i)/2.0)) * 64.0 + 128.0
                            b = (math.sin((x+i)/2.0) + math.cos((y+i)/1.5)) * 64.0 + 128.0
                            r = max(0, min(255, r + offset))
                            g = max(0, min(255, g + offset))
                            b = max(0, min(255, b + offset))
                            unicorn.set_pixel(x,y,int(r),int(g),int(b))
            unicorn.show()
            time.sleep(0.05)

while True:
    nhs()
    rainbow(75)

