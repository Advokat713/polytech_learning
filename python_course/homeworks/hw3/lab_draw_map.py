"""
? Задание: Вывести в консоль карту для игры в Bomberman (добавить на карту деревянные стены и пустоты в случайных свободных точках пространства)
"""
import random


map_lenght = 15    
map_height = 15
map_elem = ' '


# Заполнение матрицы данными
# значение ячейки = 1 - случайная стена красного цвета на карте
matrix = [[random.randint(1, 3) for i in range(map_lenght)] for j in range(map_height)]


# Строим границы карты
# значение ячейки = 0 - зафиксированная стена серого цвета
for i in range(0, map_lenght):
    matrix[0][i] = 0
    matrix[map_height-1][i] = 0

for i in range(0, map_height):
    matrix[i][0] = 0
    matrix[i][map_lenght-1] = 0

for i in range(2, len(matrix), 2):
    for j in range(2, len(matrix[i]), 2):
        matrix[i][j] = 0


#  Вывод матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            print("\033[1;30;47m {} \033[0m".format(map_elem), end="")
        elif matrix[i][j] == 1:
            print("\033[1;30;41m {} \033[0m".format(map_elem), end="")
        else:
            print("\033[1;30;40m {} \033[0m".format(map_elem), end="")
    print()