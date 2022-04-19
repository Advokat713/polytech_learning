"""
? Задание: Вывести на экран интересный рисунок с помощью черепашьей графики
"""
import turtle 


spiral = turtle.Turtle()

for i in range(50):
    spiral.forward(i * 10)
    spiral.right(144)
    
turtle.done()