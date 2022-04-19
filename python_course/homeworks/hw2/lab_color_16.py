"""
? Задание: Вывести в консоль все доступные цвета и фоны
"""


print("Текст в консоли python можно раскрасить в 8 стандартных цветов:")

for elem in range(30, 38):
    print(f"\033[1;{elem}m код цвета: {elem}\033[0m", end="")

print("\nЗадать для текста можно и цвет заливки заднего фона:")


for elem in range(40, 48):
    print(f"\033[1;30;{elem}m код заливки: {elem}\033[0m", end="")

print("\nВывод таблицы возможных вариантов цветов и заливок:")


for cl_elem in range(30, 38):
    
    for bg_elem in range(40, 48):
        print(f"\033[{cl_elem};{bg_elem}m {cl_elem}::{bg_elem}\033[0m", end="")
    
    print()
