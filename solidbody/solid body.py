from tkinter import *
from math import *
import random

master = Tk()
w = 500
w1 = 300
h = 500
h1 = 300
canvas = Canvas(master, height=w, width=h, bg='white')


class body:
    def __init__(self, coords, x, y):
        self.coords = coords
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.w = 0
        self.b = 0
        self.ax = 0
        self.ay = 0

def meme(event):
    pass


master.bind('<Button-1>', meme)
canvas.pack()
