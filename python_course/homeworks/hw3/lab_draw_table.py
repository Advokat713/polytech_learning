"""
? Задание: Вывести в консоль таблицу из ascii символов с параметрами кол-ва строк и столбцов.
https://unicode-table.com/ru/blocks/box-drawing/
"""
# Описание элементов одинарной рамки
tb = {
    'tb_hor_top': '\u252c',
    'tb_hor_bot': '\u2534',
    'tb_ver_lft': '\u251c',
    'tb_hor_rgt': '\u2524',
    'tb_angle1': '\u250c',
    'tb_angle2': '\u2510',
    'tb_angle3': '\u2518',
    'tb_angle4': '\u2514',
    'tb_center': '\u253c'
}

print("Длинна и высота рамки должна быть > 1")

tb_lenght = 1 + int(input("Введите длинну рамки "))    
tb_height = 1 + int(input("Введите высоту рамки "))


# Алгоритм построения рамки
matrix = [[tb['tb_center'] for i in range(tb_lenght)] for j in range(tb_height)]


# Заполняем угловые элементы
matrix[0][0] = tb['tb_angle1']
matrix[0][tb_lenght-1] = tb['tb_angle2']
matrix[tb_height-1][tb_lenght-1] = tb['tb_angle3']
matrix[tb_height-1][0] = tb['tb_angle4']

# Заполнение горизонтальных линий 
for i in range(1, tb_lenght-1):
    matrix[0][i] = tb['tb_hor_top']
    matrix[tb_height-1][i] = tb['tb_hor_bot']

# Заполнение вертикальных линий 
for j in range(1, tb_height-1):
    matrix[j][0] = tb['tb_ver_lft']
    matrix[j][tb_lenght-1] = tb['tb_hor_rgt']

#  Вывод матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end="")
    print()
