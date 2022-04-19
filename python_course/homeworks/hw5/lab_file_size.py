"""
? Задание: выполнить следующий набор задач:
1) Добавить столбец отображения размера файла только в Мб
2) Добавить столбец отображения размера файла по разрядно (00 000)
3) Добавить столбец отображения размера файла автоматически (в байтах, Кб, Мб, Гб)
"""

import os


def make_discharge(file_size):
    temp = str(file_size)[::-1]
    discharge = ' '.join(temp[i:i+3] for i in range(0, len(temp), 3))[::-1]
    return discharge


def choise_units(file_size):
    string = ''
    if file_size < 1024:
        string = f'{file_size} bytes'
    elif file_size >= 1024 and file_size < 1048576:
        string = f'{round(file_size / 1024, 2)} Kb'
    elif file_size >= 1048576 and file_size < 1073741824:
        string = f'{round(file_size / 1024**2, 2)} Mb'
    else:
        string = f'{round(file_size / 1024**3, 2)} Gb'
    return string    


# os.chdir('ENTER YOUR DIR')
print(os.getcwd())

for item in os.listdir():
    if not os.path.isfile(item):
        continue
    
    file_size = os.path.getsize(item)
    size_mb = round(file_size / 1024**2, 2)
    size_discharge = make_discharge(file_size)
    auto_size = choise_units(file_size)
    print(f'{item:30} | {file_size:15} bytes | {size_mb:15} Mb | {size_discharge:15} | {auto_size:15}')

