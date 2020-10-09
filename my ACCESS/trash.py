from tkinter import*
master= Tk()
def meme(event):
    print(event.keysym)
master.bind('<KeyPress>', meme)
master.mainloop()
