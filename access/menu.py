from GUI_table import representation
from tkinter import*
from tkinter import messagebox
import csv

main_menu = Tk()
#representation([['1','2'],['3','4']])
Text1 = Label(main_menu, text = "Welcom to my own DBMS", borderwidth = 2, relief = 'flat', font = ('Courier', 44))
empty1 = Label(main_menu)
empty1.grid(row=1, column = 2)
empty2 = Label(main_menu)
empty2.grid(row=3, column = 2)
empty3 = Label(main_menu)
empty3.grid(row=4, column = 2)
empty4 = Label(main_menu)
empty4.grid(row=6, column = 2)
Text1.grid(row = 2, column=4)
students = [['Шарраш У.Ю.', '9', '36'], ['Иванов А.И.', '7', '1'], ['Керк В.И.', '7', '2'], ['Торгов Л.А.', '7', '3'], ['Нанна Г.Т.', '7', '4'], ['Икрочкин Д.В.', '7', '5'], ['Кортова К.П.', '7', '6'], ['Лескин В.В.', '7', '7'], ['Тортин Г.А.', '7', '8'], ['Шпэкс А.Г.', '7', '9'], ['Улицына Е.Ю.', '7', '10'], ['Мусатов О.Ю.', '8', '11'], ['Герфорт И.Г.', '8', '12'], ['Калькина Д.И.', '8', '13'], ['Рябинин К.Н.', '8', '14'], ['Неверкина А.К.', '8', '15'], ['Быков А.Е.', '8', '16'], ['Аляпина Т.П.', '8', '17'], ['Романенко Р.Р.', '8', '18'], ['Витас Д.А.', '8', '19'], ['Шарочкина Е.Н.', '8', '20'], ['Кольцева П.А.', '9', '21'], ['Куркуров К.К.', '9', '22'], ['Лянин И.А.', '9', '23'], ['Евнушенко Т.Т.', '9', '24'], ['Пилатова Е.В.', '9', '25'], ['Кольтс П.П.', '9', '26'], ['Уряденко А.Л.', '9', '27'], ['Шпротский Е.И.', '9', '28'], ['Цукен Г.В.', '9', '29'], ['Венерова Л.Н.', '9', '30'], ['Щучкина Ю.Б.', '7', '31'], ['Лапленд Е.П.', '8', '32'], ['Глеск Д.Д.', '9', '33'], ['Фожкрунт Д.Я.', '7', '34'], ['Восемсотпятдесятвторой Д.О.', '8', '35']]
dict_stud = {'name': ['Шарраш У.Ю.', 'Иванов А.И.', 'Керк В.И.', 'Торгов Л.А.', 'Нанна Г.Т.', 'Икрочкин Д.В.', 'Кортова К.П.', 'Лескин В.В.', 'Тортин Г.А.', 'Шпэкс А.Г.', 'Улицына Е.Ю.', 'Мусатов О.Ю.', 'Герфорт И.Г.', 'Калькина Д.И.', 'Рябинин К.Н.', 'Неверкина А.К.', 'Быков А.Е.', 'Аляпина Т.П.', 'Романенко Р.Р.', 'Витас Д.А.', 'Шарочкина Е.Н.', 'Кольцева П.А.', 'Куркуров К.К.', 'Лянин И.А.', 'Евнушенко Т.Т.', 'Пилатова Е.В.', 'Кольтс П.П.', 'Уряденко А.Л.', 'Шпротский Е.И.', 'Цукен Г.В.', 'Венерова Л.Н.', 'Щучкина Ю.Б.', 'Лапленд Е.П.', 'Глеск Д.Д.', 'Фожкрунт Д.Я.', 'Восемсотпятдесятвторой Д.О.'], 'class': ['9', '7', '7', '7', '7', '7', '7', '7', '7', '7', '7', '8', '8', '8', '8', '8', '8', '8', '8', '8', '8', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '7', '8', '9', '7', '8'], 'id_student': [36, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]}
teachers = [['Дамблдор А.А.', 'Защитаоттемныхискусств', '14'], ['Локонс Б.И.', 'Защитаоттемныхискусств', '1'], ['Люпин К.Б.', 'Защитаоттемныхискусств', '2'], ['Квиррел К.Н.', 'Защита', 'от'], ['МакГонагалл М.В.', 'Трансфигурация', '4'], ['Снегг С.С.', 'Зельеварение', '5'], ['Вектор Е.С.', 'Астрономия', '6'], ['Спраут Е.Ф.', 'Травология', '7'], ['Флитвик Ф.Ф.', 'Заклинания', '8'], ['Снегг С.С.', 'Защитаоттемныхискусств', '9'], ['Дамблдор А.А.', 'Трансфигурация', '10'], ['Слизнорт Г.И.', 'Зельеварение', '11'], ['Трюк М.А.', 'Полетынаметле', '12'], ['Трелони А.И.', 'Прорицания', '13']]
dict_teach = {'name': ['Дамблдор А.А.', 'Локонс Б.И.', 'Люпин К.Б.', 'Квиррел К.Н.', 'МакГонагалл М.В.', 'Снегг С.С.', 'Вектор Е.С.', 'Спраут Е.Ф.', 'Флитвик Ф.Ф.', 'Снегг С.С.', 'Дамблдор А.А.', 'Слизнорт Г.И.', 'Трюк М.А.', 'Трелони А.И.'], 'subject': ['Защитаоттемныхискусств', 'Защитаоттемныхискусств', 'Защитаоттемныхискусств', 'Защитаоттемныхискусств', 'Трансфигурация', 'Зельеварение', 'Астрономия', 'Травология', 'Заклинания', 'Защитаоттемныхискусств', 'Трансфигурация', 'Зельеварение', 'Полетынаметле', 'Прорицания'], 'id_s_t': [14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}


def journal():
    with open('marks.csv') as marks:
        marks_list = csv.reader(marks, delimiter = ';')
        marks_dict = csv.DictReader(marks, delimiter = ';')
        matrix = []
        for i in marks_list:
            matrix.append(i)
    repres = [['01/09/2019', '02/09/2019, 03/09/2019']]
    def ok():
        if (login.get() == password.get()) and login.get().isalnum() and password.get().isalnum() and your_class.get().isalnum():
            if int(login.get()) in dict_teach['id_s_t'] and int(your_class.get()) in [7,8,9]:
                cl = your_class.get()
                for i in matrix[1:]:
                    if cl==i[1] and login.get() == i[3]:
                        if i[4] == '01/09/2019':
                            pass
                        if i[4] == '01/09/2019':
                            pass
                        if i[4] == '01/09/2019':
                            pass


            else:
                messagebox.showinfo('DBMS', 'Error')
        else:
            messagebox.showinfo('DBMS', 'Error')
    question = Tk()
    question.geometry("500x200")
    login = StringVar(question)
    password = StringVar(question)
    your_class=StringVar(question)
    login_label = Label(question, text  = 'login:')
    password_label = Label(question, text  = 'password:')
    class_label = Label(question, text  = 'class:')
    login_entry = Entry(question, textvariable=login)
    password_entry = Entry(question, textvariable=password)
    class_entry = Entry(question, textvariable=your_class)

    login_entry.place(relx=.7, rely=.1, anchor="c")
    password_entry.place(relx=.7, rely=.3, anchor="c")
    login_label.place(relx=.2, rely=.1, anchor="c")
    password_label.place(relx=.2, rely=.3, anchor="c")
    class_entry.place(relx=.2, rely=.6, anchor="c")
    ok_button = Button(question, text="Click Me", command=ok)
    ok_button.place(relx=.5, rely=.5, anchor="c")

    question.mainloop()
def timetable():
    pass
Button_journal = Button(main_menu, text='Журнал', command = journal,  font = ('Courier', 44), borderwidth = 10, relief = 'ridge')
Button_journal.grid(row = 5, column = 3)
Button_timetable=Button(main_menu, text='Расписание', command = timetable,  font = ('Courier', 44), borderwidth = 10, relief = 'ridge')
Button_timetable.grid(row=5, column=8)
main_menu.mainloop()