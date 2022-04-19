"""
? Задание: Вывести на экран интересный рисунок с помощью черепашьей графики
"""
from turtle import *


color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)
    
    if abs(pos()) < 1:
        break

end_fill()

done()