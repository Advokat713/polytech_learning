"""
? Задание: выполнить следующий набор задач:
1) Топ 5
2) Топ самых часто используемых имен файлов
3) Топ самых часто используемых расширений файлов
4) Топ самых больших файлов
5) Топ самых маленьких файлов
6) Топ самых длинных имен файлов
7) Топ самых длинных расширений файлов
8) Топ самых коротких имен файлов
9) Топ самых коротких расширений файлов
"""

import os
from typing import Counter

# os.chdir('ENTER YOUR DIR')

def top_five(counter_data, info, sort_side='max'):
    counter_data = dict(counter_data)
    sorted_dict = {}
    if sort_side == 'max':
        sorted_keys = sorted(counter_data, key=counter_data.get, reverse=True)
    else:
        sorted_keys = sorted(counter_data, key=counter_data.get, reverse=False)
    
    for w in sorted_keys:
        sorted_dict[w] = counter_data[w]
    
    i = 0
    print(f'Топ 5 {info}:')
    for key, value in sorted_dict.items():
        i += 1
        if i <= 5:
            print(f'{repr(key):5} - {value}')
    print("__________________________________________________")


files_sizes = {}
names_lenghts = {}
exp_lenghts = {}


# Формирую дополнительные словари ключ-значение для удобной сортировки
for item in os.listdir():
    if not os.path.isfile(item):
        continue

    files_sizes[f'{item}'] = os.path.getsize(item)
    names_lenghts[f'{item}'] = len(item.split('.')[0])
    exp_lenghts[f'{item}'] = len(item.split('.')[-1])


# Создаю список расширений и имен в указанной директории
names_list = [item.split('.')[0] for item in os.listdir()]
exp_list = [item.split('.')[-1] for item in os.listdir()]


c_names = Counter(names_list)
c_exp = Counter(exp_list)


# Вызов функции сортировки и вывода в консоль результатов
top_five(c_names, 'имен')
top_five(c_exp, 'расширений')
top_five(files_sizes, 'больших размеров')
top_five(files_sizes, 'маленьких размеров', 'min')
top_five(names_lenghts, 'больших длинн имён')
top_five(names_lenghts, 'маленьких длинн имён', 'min')
top_five(exp_lenghts, 'больших длинн расширений')
top_five(exp_lenghts, 'маленьких длинн расширений', 'min')
