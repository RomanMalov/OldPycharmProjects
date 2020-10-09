from tkinter import *
from tkinter import messagebox
def y():
    def x():
        with open('marks.csv') as marks:
            def show_message():
                messagebox.showinfo("GUI Python", mes.get())


            root = Tk()
            root.geometry("300x250")
            mes=StringVar()
            mes1=StringVar()

            message_entry = Entry(root, textvariable = mes)
            message_entry1 = Entry(root, textvariable = mes1)

            message_entry.place(relx=.5, rely=.1, anchor="c")
            message_entry1.place(relx=.5, rely=.3, anchor="c")

            message_button = Button(text="Click Me", command=show_message)
            message_button.place(relx=.5, rely=.5, anchor="c")

            root.mainloop()
    x()
y()
