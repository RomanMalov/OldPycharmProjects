from tkinter import*
import numpy as np

def representation(tabl):
    table=tabl
    master = Tk()
    xychange=[0, 0]
    #ychange=0
    y=len(table)
    x=len(max(table, key = len))
    coords = [x, y]
#canvas = Canvas(master, width=50*x, height=30*y, bg='white')

    list_of_labels=[]
    for i in range(coords[1]):
        new_line=[]
        for j in range(coords[0]):
            new_line.append(Label(master,  text=str(table[i][j]), width=8, height=3, borderwidth=2, relief='ridge'))
        list_of_labels.append(new_line)
    for i in range(coords[1]):
        for j in range(coords[0]):
            (list_of_labels[i][j]).grid(row=i, column=j)
    def change(event):

        x = (master.winfo_pointerx()-master.winfo_rootx())
        y =(master.winfo_pointery()-master.winfo_rooty())
        xychange[0] = x//79
        xychange[1] = y//55

    def enter(event):
        #global list_of_labels
        tx = table[xychange[1]][xychange[0]]
        if event.keysym=='BackSpace':
            if bool(tx):
                tx=tx[:-1]
        else:
            tx+=event.char
        table[xychange[1]][xychange[0]]=tx
        list_of_labels[xychange[1]][xychange[0]].config(text=tx)
    def new_row():
        coords[1]+=1
        new_list = []
        new_line=[]
        for j in range(coords[0]):
            new_list.append('')
            new_line.append(Label(master,  text='', width=8, height=3, borderwidth=2, relief='ridge'))
        list_of_labels.append(new_line)

        for j in range(coords[0]):
            (list_of_labels[coords[1]-1][j]).grid(row=coords[1], column=j)

        tabl.append(new_list)
    add_row=Button(master, text = 'Add row', command = new_row)
    add_row.grid(row = coords[1]//2, column = coords[0]+1)
    master.bind('<KeyPress>', enter)
    master.bind('<Button-1>', change)
    master.mainloop()
    return tabl
x= representation([['1','2','4'],['3','4', '5']])
    