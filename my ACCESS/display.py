from tkinter import*
import math
import numpy
matrix = [['1','2', '0'],['1',' 2', '3'],['1','2','3']]
master= Tk()
x = len(matrix[0])
y = len(matrix)
list_of_labels=[]
changex=0
changey=0
for i in range(y):
    low_list=[]
    for j in range(x):
        low_list.append(Label(master, text=matrix[i][j], height=5, width=5, borderwidth=4, relief='ridge'))
    list_of_labels.append(low_list)
for i in range(y):
    for j in range(x):
        list_of_labels[i][j].grid(row=i, column =j)
def enter(event):
    global matrix
    l=matrix[changey][changex]
    if event.keysym=='BackSpace':
        if bool(l):
            l=l[:-1]
    else:
        l+=event.char        
    matrix[changey][changex]=l
    list_of_labels[changey][changex].config(text=l)
def change(event):
    pass
master.bind('<KeyPress>', enter)
master.bind('<Button-1>', change)
master.mainloop()
