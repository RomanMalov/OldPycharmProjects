import tkinter
master = tkinter.Tk()
canvas=tkinter.Canvas(master, height = 500, width = 500)
def proc():
    print('lox')
def proc1():
    print('nelox')
but1 = tkinter.Button(master, text = 'text', height = 2, width = 20, command = proc1)
but= tkinter.Button(master, text = 'text', height = 20, width = 20, command = proc)
canvas.pack()
but.pack()
but1.pack()
master.mainloop()
