from tkinter import*
master = Tk()
a=255
b=255
c=255
da=0
db=0
dc=0
flag = True

clr1='#'+('000'+str(hex(a%256))[2:])[-2:]+('000'+str(hex(b%256))[2:])[-2:]+('000'+str(hex(c%256))[2:])[-2:]
clr2='#'+('000'+str(hex((a+da)%256))[2:])[-2:]+('000'+str(hex((b+db)%256))[2:])[-2:]+('000'+str(hex((c+dc)%256))[2:])[-2:]

canvas = Canvas(master, height=700, width=700)
s1=canvas.create_rectangle(0,0,400,800, fill = clr1)
s2=canvas.create_rectangle(400,0,800,800, fill = clr2,outline=clr2)
s = canvas.create_rectangle(650,650,700,700, fill = 'black')

canvas.pack()
def meme(event):
    global a , b, c, flag, da, db, dc
    if event.char=='q':
        flag = not flag
        canvas.itemconfig(s, fill= ('black' if flag else 'white'))
    if flag:
        if event.char=='a':
            a+=1
        if event.char=='z':
            a-=1
        if event.char=='s':
            b+=1
        if event.char=='x':
            b-=1
        if event.char=='d':
            c+=1
        if event.char=='c':
            c-=1
        if event.char=='p':
            print(a,b,c)
    else:
        if event.char == 'a':
            da += 1
        if event.char == 'z':
            da -= 1
        if event.char == 's':
            db += 1
        if event.char == 'x':
            db -= 1
        if event.char == 'd':
            dc += 1
        if event.char == 'c':
            dc -= 1
        if event.char == 'p':
            print(da, db, dc)
    clr1 = '#' + ('000'+str(hex(a % 256))[2:])[-2:] + ('000'+str(hex(b % 256))[2:])[-2:] + ('000'+str(hex(c % 256))[2:])[-2:]
    clr2 = '#' + ('000'+str(hex((a + da) % 256))[2:])[-2:] + ('000'+str(hex((b + db) % 256))[2:])[-2:] + ('000'+str(hex((c + dc) % 256))[2:])[-2:]

    canvas.itemconfig(s1, fill = clr1)
    canvas.itemconfig(s2,fill = clr2,outline=clr2)

master.bind('<KeyPress>',meme)
master.mainloop()