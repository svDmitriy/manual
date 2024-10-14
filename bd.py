from tkinter import * #для работы с окнами
def setwindow(root):
    root.title("База данных")  # назваине окна
    root.resizable(False, False)  # при True -можно менять размер окна
    icon = PhotoImage(file='logo.png')#идентификация фавиконки
    root.iconphoto(True, icon)#вывод изображения



    w = 500
    h = 300  # высота окна
    ws = root.winfo_screenmmwidth()
    wh = root.winfo_screenheight()  # высота экрана

    x = int(ws / 2 - w / 2)  # сдвиг влево на пол окна
    y = int(wh / 2 - h / 2)  # сдвиг вверх на пол окна

    root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))  # По центру окна

root = Tk()  # создано окно
setwindow(root)

#Метка программы
label1 = Label(root, text="Поиск", font="Tahoma 25", bg="#ececec")
label1.grid(row=0, column=1, padx=25, pady=25)

#надписи
label2 = Label(root, text="Фамилия:", font="Tahoma 20", bg="#ececec")
label2.grid(row=1, column=0, sticky="nw")

label3 = Label(root, text="Имя:", font="Tahoma 20", bg="#ececec")
label3.grid(row=2, column=0, rowspan=2, sticky="w")

#Логин
entry1 = Entry(root, font="Tahoma 20", bg="white", fg="black", bd=1)#Текстовое поле
entry1['font'] = 'Tahoma 20'
entry1.grid(row=1, column=1, sticky="se")#вывод поля на экран

#Пароль
entry2 = Entry(root, font="Tahoma 20", bg="white", fg="black", bd=1, show="*")#Текстовое поле(*-шифрует текст)
entry2.insert(END, "")
entry2.grid(row=2, column=1,sticky="se")#вывод поля на экран

#кнопка
button1 = Button(root, text="Войти", bg="White", fg="black", font="Tahoma 18")#Добавление кнопки
button1.grid(row=6, column=1,sticky="se")#Вывод кнопки на экран

root.mainloop()  # отображение окна(бесконечный цикл)