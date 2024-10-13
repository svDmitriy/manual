from tkinter import * #для работы с окнами

root = Tk()#создано окно
root.title("Окно программы")#назваине окна
root.resizable(False, False)#при True -можно менять размер окна

w = 800
h = 600 #высота окна
ws = root.winfo_screenmmwidth()
wh = root.winfo_screenheight() #высота экрана
print(ws, wh) #известна ширина и высота окна у пользователя

x = int(ws / 2 - w / 2) #сдвиг влево на пол окна
y = int(wh / 2 - h / 2) #сдвиг вверх на пол окна


#root.geometry("800x600+700+400")#размеры

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))#По центру окна


root.mainloop()#отображение окна(бесконечный цикл)



