"""
? Задание: Вывести на экран интересный рисунок с помощью черепашьей графики
"""
import turtle


wn = turtle.Screen()
wn.bgcolor('black')


# Albert
Albert = turtle.Turtle()
Albert.speed(0)
Albert.color('white')
rotate = int(360)


def drawCircles(t, size):

    for i in range(10):
        t.circle(size)
        size -= 4


def drawCpecial(t, size, repeat):

    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawCpecial(Albert, 100, 10)


# Steve
Steve = turtle.Turtle()
Steve.speed(0)
Steve.color('yellow')
rotate = int(90)


def drawCircles(t, size):

    for i in range(4):
        t.circle(size)
        size -= 10


def drawCpecial(t, size, repeat):

    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawCpecial(Steve, 100, 10)


# Bill
Bill = turtle.Turtle()
Bill.speed(0)
Bill.color('blue')
rotate = int(60)


def drawCircles(t, size):

    for i in range(4):
        t.circle(size)
        size -= 5


def drawCpecial(t, size, repeat):

    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawCpecial(Bill, 100, 10)


# Will
Will = turtle.Turtle()
Will.speed(0)
Will.color('red')
rotate = int(140)


def drawCircles(t, size):

    for i in range(4):
        t.circle(size)
        size -= 20


def drawCpecial(t, size, repeat):

    for i in range(repeat):
        drawCircles(t, size)
        t.right(360/repeat)


drawCpecial(Will, 100, 10)

turtle.getscreen()._root.mainloop()
