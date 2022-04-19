"""
? Задание: Вывести на экран прямоугольник с задаными параметрами ширины и длинны
"""
import turtle


length = int(input("Введите длинну прямоугольника:  "))
width = int(input("Введите ширину прямоугольника:  "))

turtlePen = turtle.Turtle()
window = turtle.Screen()

turtlePen.forward(length)
turtlePen.left(90)
turtlePen.forward(width)
turtlePen.left(90)
turtlePen.forward(length)
turtlePen.left(90)
turtlePen.forward(width)

window.mainloop()