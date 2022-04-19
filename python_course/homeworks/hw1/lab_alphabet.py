"""
? Задание: Вывести в консоль алфавит через пробел различными способами
"""
import string


# Простой вывод алфавита из строковой переменной
def print_alphabet(alphabet):

    for char in alphabet:
        print(char + " ", end="")

    print()


# Вывод алфавита через обращение к коду ASCII
def print_ascii():
    alphabet = []
    
    for i in range (65, 91):
        alphabet.append(chr(i))

    print(alphabet)
    print()


# Вывод алфавита с использованием функции map
def print_map():
    alphabet = list(map(chr, range(97, 123)))
    
    print(alphabet)
    print()


# Вывод алфавита с использованием модуля string
def print_string():
    lowercase_alphabets=list(string.ascii_lowercase)
    
    print(lowercase_alphabets)


print_alphabet("abcdefghijklmnopqrstuvwxyz")
print_ascii()
print_map()
print_string()