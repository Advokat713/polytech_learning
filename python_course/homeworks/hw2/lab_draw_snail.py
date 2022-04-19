"""
? Задание: Вывести в консоль улитку с заданной длинной и высотой
"""
import math


elem = "[]"
size = 1


# Проверка ввода размерности матрицы 
while size < 9 or size > 100:
    print("Размер улитки должен быть >= 9 и <= 100")
    size = int(input("Укажите размер улитки? "))

spiral_nums = math.floor(math.sqrt(size))

# Создание матрицы
matrix = [[0 for i in range(size)] for j in range(size)]


# Вывод матрицы
def print_matrix(matrix, elem):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                print(f"\033[1;30;40m{elem}\033[0m", end="")
            else:
                print(f"\033[1;30;47m{elem}\033[0m", end="")    
        print ()


# Заполнение матрицы
def fill_matrix(matrix, str_num_1, str_num_2, col_num_1, col_num_2):
    # верхняя линия
    for j in range(col_num_1, col_num_2):
        matrix[str_num_1][j] = 1
    
    # нижняя линия
    for j in range(col_num_1, col_num_2):
        matrix[str_num_2][j] = 1
    
    # правая линия
    for i in range(str_num_1, str_num_2):
        matrix[i][col_num_2-1] = 1

    # левая линия
    for i in range(str_num_1+2, str_num_2):
        matrix[i][col_num_1] = 1
    
    # закрасить соединяющий блок
    matrix[str_num_1+2][col_num_1+1] = 1


# Вызов функций
step = 0
for i in range(spiral_nums):
    fill_matrix(matrix, str_num_1=step, str_num_2=size-1-step, col_num_1=step, col_num_2=size-step)
    step += 2

#Заполнение матрицы происходит с шагом 2 
# fill_matrix(matrix, str_num_1=0, str_num_2=size-1, col_num_1=0, col_num_2=size)
# fill_matrix(matrix, str_num_1=2, str_num_2=size-3, col_num_1=2, col_num_2=size-2)


# Вывод получившейся матрицы
print_matrix(matrix, elem)
