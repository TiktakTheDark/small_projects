# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 01:30:56 2020

@author: Gregory
"""
import numpy as np
from PIL import Image

PIXEL_SCALE = 200
WIDTH = 3
HEIGHT = 3
XSTART = -2
YSTART = -1.5

image_width = int(PIXEL_SCALE*WIDTH)
image_height = int(PIXEL_SCALE*HEIGHT)

def create_color(v):
    values = [0, 64, 128, 196]
    b = values[v % 4] 
    g = values[(v//4) % 4] 
    r = values[(v//16) % 4]
    return (r, g, b)


def calc(c1, c2):
    x = y = 0
    for i in range(1000):
        x, y = x*x - y*y + c1, 2*x*y + c2
        if x*x + y*y > 4:
            return i+1
    return 0

array = np.zeros((image_height,
                  image_width,
                  3),
                 dtype=np.uint8)

for i in range(image_width):
    c1 = XSTART + i/PIXEL_SCALE
    for j in range(image_height):
        c2 = YSTART + j/PIXEL_SCALE
        v = calc(c1, c2)
        array[j, i,] = create_color(v)

img = Image.fromarray(array)
img.save('mandelbrot-colour.png')