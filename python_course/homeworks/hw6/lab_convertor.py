"""
? Задание: сделать простой конвертор велечин с помощью GUI - Tkinter
"""
from tkinter.constants import END
import tkinter as tk


def convert():
    c = int(e1.get())
    f = ((c*9)/(5))+32
    t1.config(state='normal')
    t1.delete('1.0', END)
    t1.insert(END,f)
    t1.config(state='disabled')


def clear_all():
    e1.delete(0, END)
    t1.config(state='normal')
    t1.delete("1.0", END)
    t1.config(state='disabled')


window = tk.Tk()
window.geometry("300x250")
window.config(bg="#BCBABE")
window.resizable(width=False,height=False)
window.title('Конвертор величин')


l2= tk.Label(window,text="Введите величину в Цельсиях: ",font=("Arial", 10,"bold"),fg="#2F2E33",bg="#BCBABE")
l3= tk.Label(window,text="Значение по Фаренгейту равно: ",font=("Arial", 10,"bold"),fg="#2F2E33",bg="#BCBABE")

# Пустые поля для разграничения элементов управления формой
empty_l1 = tk.Label(window,bg="#BCBABE")
empty_l2 = tk.Label(window,bg="#BCBABE")

e1= tk.Entry(window,font=('Arial',10))
t1=tk.Text(window,state="disabled",width=15,height=0)

btn1 = tk.Button(window,text="Конвертировать!",font=("Arial", 10),command=convert)
btn2 = tk.Button(window,text="Очистить поля",font=("Arial", 10),command=clear_all)


l2.pack()
e1.pack()
empty_l1.pack()
btn1.pack()
l3.pack()
t1.pack()
empty_l2.pack()
btn2.pack()


# Запуск цикла отображения окна приложения
window.mainloop()