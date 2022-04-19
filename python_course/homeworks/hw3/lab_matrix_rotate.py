"""
? Задание: Создать двумерный массив, заполнив его набором случайных значений от 10 до 99.
? Распечатать его в консоль, а затем в цикле выбирать действие (повернуть в лево, в право, отразить)
? а затем распечатать в консоль результат выполнения работы
"""
import random


# Вывод матрицы в консоль
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("\033[1;30;47m {} \033[0m".format(matrix[i][j]), end="")
        print()


#  Повернуть массив
def rotate_matrix(matrix, side):
    if side == "right":
        matrix = tuple(zip(*matrix[::-1]))
    else:
        matrix = tuple(zip(*matrix))[::-1]

    return matrix


# Заменить четные числа на 95 
def replace_even(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 95

    return matrix


# Отразить массив
def reflect_matrix(matrix):
    # Замена всех элементов массива на зеркальные 21 -> 12, 45 -> 54
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            revs_elem = 0
            number = matrix[i][j]

            while (number > 0):
                remainder = number % 10
                revs_elem = (revs_elem * 10) + remainder
                number = number // 10

            matrix[i][j] = revs_elem

    print_matrix(matrix)


size = 0

while size <= 1:
    print("Длинна массива должна быть > 1")
    size = int(input("Введите длинну массива: "))

# генерация двумерного массива с случайными значениями
# при генерации идет исключение всех чисел заканчивающихся на 0 (10, 20, ... , 90) для удобства работы с преобразованиями над массивом
matrix = [[random.randint(1, 9)*10 + random.randint(1, 9)
           for i in range(size)] for j in range(size)]

print_matrix(matrix)

command = "go"

# Цикл для определения действий над массивом
while command != "stop":
    command = input("""Напиши:\n 1 - чтобы повернуть массив в лево 
                    \n 2 - чтобы повернуть массив в право 
                    \n 3 - чтобы отразить массив 
                    \n 4 - чтобы заменить все четные значения на 95
                    \n stop - чтобы завершить программу """)

    # конструкция switch-case python
    match command:
        case "1":
            side = "left"
            matrix = rotate_matrix(matrix, side)
            print_matrix(matrix)
        case "2":
            side = "right"
            matrix = rotate_matrix(matrix, side)
            print_matrix(matrix)
        case "3":
            reflect_matrix(matrix)
        case "4":
            matrix = replace_even(matrix)
            print_matrix(matrix)
