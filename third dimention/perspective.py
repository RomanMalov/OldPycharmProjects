from tkinter import*
from math import*
master = Tk()
camera_width = 600
camera_height = 600
focal_length =  50
def vectormultiply(coords0, coords1):
    x0,y0,z0 = coords0
    x1,y1,z1 = coords1
    return [y0*z1-z0*y1, z0*x1-x0*z1, x0*y1-y0*x1]
    

canvas = Canvas(master, width = camera_width, height = camera_height)
canvas.pack()

master.mainloop()