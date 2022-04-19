"""
? Задание: Вывести в консоль змейку с заданной длинной и высотой
"""


lenght = int(input("Введите длинну змейки"))
height = int(input("Введите высоту змейки"))
tail = True
elem = "()()"

print(f"Змейка длинной {lenght} и высотой {height}:")

for str_num in range(0, height):
    if str_num % 2 == 0:
        for col_num in range(0, lenght):
            print(f"\033[1;37;47m{elem}\033[0m", end="")
    else:
        if tail:
            for col_num in range(0, lenght - 1):
                print(f"\033[1;30;40m{elem}\033[0m", end="")
            print(f"\033[1;37;47m{elem}\033[0m", end="")
            tail = False
        else:
            print(f"\033[1;37;47m{elem}\033[0m", end="")
            for col_num in range(0, lenght - 1):
                print(f"\033[1;30;40m{elem}\033[0m", end="")
            tail = True
    print()

print("Вот такая вот змейка получилась:)")
