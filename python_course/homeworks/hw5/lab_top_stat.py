"""
? Задание: выполнить следующий набор задач:
1) Показать статистику всех символов
2) Показать статистику всех символов в порядке убывания
3) Показать статистику всех цифр в порядке убывания
4) Показать статистику всех английских букв в порядке уменьшения (все буквы должны быть и напротив кол-во встречаний)
"""

from typing import Counter


def sort_stat(counter_data):
    counter_data = dict(counter_data)
    sorted_dict = {}
    sorted_keys = sorted(counter_data, key=counter_data.get, reverse=True)
    
    for w in sorted_keys:
        sorted_dict[w] = counter_data[w]

    for key, value in sorted_dict.items():
        print(f'{repr(key):5} - {value}')
    print("__________________________________________________")


def sort_numbers(counter_data):
    counter_data = dict(counter_data)
    sorted_dict = {}
    sorted_keys = sorted(counter_data, key=counter_data.get, reverse=True)
    
    for w in sorted_keys:
        sorted_dict[w] = counter_data[w]

    for key, value in sorted_dict.items():
        if str(key).isnumeric():
            print(f'{repr(key):5} - {value}')
    print("__________________________________________________")


def sort_english(counter_data):
    alphabet = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'}
    counter_data = dict(counter_data)
    sorted_dict = {}
    sorted_keys = sorted(counter_data, key=counter_data.get, reverse=True)
    
    for w in sorted_keys:
        sorted_dict[w] = counter_data[w]

    for key, value in sorted_dict.items():
        if str(key).upper() in alphabet:
            print(f'{repr(key):5} - {value}')
    print("__________________________________________________")


with open("ENTER YOUR DIR", "r") as f:
    c = Counter(f.read())

    # Вывод статистики
    for key, value in c.items():
        print(f'{repr(key):5} - {value}')

    # Вывод статистики с сортировкой по убыванию
    sort_stat(c)
    # Вывод статистики цифр с сортировкой по убыванию
    sort_numbers(c)
    # Вывод букв английского алфавита со статистикой
    sort_english(c)
