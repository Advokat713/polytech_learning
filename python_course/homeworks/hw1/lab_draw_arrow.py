"""
? Задание: Вывести на экран стрелочку
"""
import turtle


length = int(input("Введите длинну стрелки:  "))
height = int(input("Введите высоту стрелки:  "))

turtlePen = turtle.Turtle()
window = turtle.Screen()

turtlePen.forward(length)
turtlePen.right(90)
turtlePen.forward(height)
turtlePen.left(135)
turtlePen.forward(length // 2)
turtlePen.left(90)
turtlePen.forward(length // 2)
turtlePen.left(135)
turtlePen.forward(height)
turtlePen.right(90)
turtlePen.forward(length)
turtlePen.left(90)
turtlePen.goto(0.00, 0.00)

window.mainloop()