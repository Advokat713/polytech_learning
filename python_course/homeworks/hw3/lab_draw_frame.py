"""
? Задание: Вывести в консоль рамку из ascii символов с параметрами длинна, ширина, толщина.
https://unicode-table.com/ru/blocks/box-drawing/
"""
# Описание элементов одинарной рамки
br = {
    'br1_hor': '\u2500',
    'br1_ver': '\u2502',
    'br1_angle1': '\u250c',
    'br1_angle2': '\u2510',
    'br1_angle3': '\u2518',
    'br1_angle4': '\u2514',
    'br2_hor': '\u2550',
    'br2_ver': '\u2551',
    'br2_angle1': '\u2554',
    'br2_angle2': '\u2557',
    'br2_angle3': '\u255d',
    'br2_angle4': '\u255a'
}

prefix = ""

print("Длинна и высота рамки должна быть > 1")

br_lenght = int(input("Введите длинну рамки "))    
br_height = int(input("Введите высоту рамки "))

print("Рамка может быть двойной или одинарной")

br_mode = int(input("Введите 1 для одинарной рамки или 2 для двойной "))


# Алгоритм построения рамки
matrix = [[' ' for i in range(br_lenght)] for j in range(br_height)]


#  Проверка модификатора рамки
if br_mode == 1:
    prefix = "br1_"
else:
    prefix = "br2_"

# Заполняем угловые элементы
matrix[0][0] = br[f'{prefix}angle1']
matrix[0][br_lenght-1] = br[f'{prefix}angle2']
matrix[br_height-1][br_lenght-1] = br[f'{prefix}angle3']
matrix[br_height-1][0] = br[f'{prefix}angle4']

# Заполнение горизонтальных линий 
for i in range(1, br_lenght-1):
    matrix[0][i] = br[f'{prefix}hor']
    matrix[br_height-1][i] = br[f'{prefix}hor']

# Заполнение вертикальных линий 
for j in range(1, br_height-1):
    matrix[j][0] = br[f'{prefix}ver']
    matrix[j][br_lenght-1] = br[f'{prefix}ver']

#  Вывод матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end="")
    print()
