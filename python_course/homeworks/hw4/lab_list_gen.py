"""
? Задание: Выполнить следующий список задач:
1) Вернуть список слов в заданной строке
2) Вернуть список слов и рядом с каждым вывести его длинну в []
3) Вернуть список слов и рядом с каждым вывести его порядковый номер в ()
4) В каждом слове поменять регистр символа на противоположный
5) В каждом слове поменять буквы местами
6) В каждом слове поменять буквы случайным образом
7) В каждом слове сделать последнюю букву заглавной
8) В каждом слове заменить первую и последнюю букву символом "_"
9) Каждое второе слово написать заглавными буквами
10) Заменить все гласные на "0"
11) Поменять слова местами случайным образом
"""
import random

text = "Нужно бежать со всех ног чтобы только оставаться на месте А чтобы куда-то попасть Надо бежать как минимум вдвое БЫСТРЕЕ"

# Список слов в строке
def list_of_words(text):
    print([word for word in text.split()])

# Список слов и их длинна
def list_with_lenght(text):
    print([f'{word}[{len(word)}]' for word in text.split()])

# Список слов и их порядковый номер
def list_with_position(text):
    print([f'{word}({i+1})' for i, word in enumerate(text.split())])

# Список слов и смена регистра на противоположный
def item_reverse_case(text):
    print([f'{word.swapcase()}' for word in text.split()])

# Список слов и смена порядка букв в них
def item_reverse_chars(text):
    print([f'{word[::-1]}' for word in text.split()])

# Список слов и смена порядка букв в них случайным образом
def random_reverse_chars(text):
    list = []
    for word in text.split():
        temp = []
        
        for char in word:
            temp.append(char)

        random.shuffle(temp)
        
        list.append(''.join(temp))
        
    print(list)

# Каждая последняя буква слова заглавная
def upper_last_char(text):
    list = []
    for item in text.split():
        item = item[::-1]
        item = item.title()
        item = item[::-1]
        list.append(item)
    
    print(list)

# В каждом слове первая и последняя заменены символом "__"
def replace_chars(text):
    list = []
    for item in text.split():
        item = item.replace(item[0], '_')
        item = item.replace(item[-1], '_')
        list.append(item)
    
    print(list)

# Каждое второе слово заглавными
def second_word_upper(text):
    list = [word for word in text.split()]
    for i, word in enumerate(list):
        # так как счет с 0, то необходимо искать нечетные позиции списка
        if i % 2 != 0:
            list[i] = word.upper() 
    
    print(list)

# Заменить все гласные на "0"
def replace_vowels(text):
    list = [word for word in text.split()]
    volwes = ('а', 'я', 'у', 'ю', 'о', 'ё', 'е', 'э', 'и', 'ы')
    for i, word in enumerate(list):
        temp = ''
        for char in word:
            if char.lower() in volwes:
                temp += '0'
            else:
                temp += char
        list[i] = temp

    print(list)


# Список слов случайным образом
def random_list(text):
    new_text = [word for word in text.split()]
    random.shuffle(new_text)
    print(new_text)


# Вызов функций
list_of_words(text)
list_with_lenght(text)
list_with_position(text)
item_reverse_case(text)
item_reverse_chars(text)
random_reverse_chars(text)
upper_last_char(text)
replace_chars(text)
second_word_upper(text)
replace_vowels(text)