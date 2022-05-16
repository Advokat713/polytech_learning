"""
? Задание: выполнить преобразования исходного цвета, взятого из пространства LAB в:
    1) LCH
    2) RGB
    3) HSV
    4) HSL
! Затем провести процесс обратного преобразования в LAB, рассчитать параметры дельта Е для полученных цветов.
"""
import math

from colormath.color_objects import LabColor, LCHabColor, AdobeRGBColor, HSLColor, HSVColor
from colormath.color_diff import delta_e_cie1994, delta_e_cie2000
from colormath.color_conversions import convert_color


# Функция для перевода из исходного LAB
def convert_from_lab(LAB):
    
    # Создаем словарь, для удобного отображения результатов конвертирования
    convert_dict = {}

    # Вносим изначальное значение
    convert_dict['LAB_color'] = LAB

    # Производим перевод в LCH
    convert_dict['LCH_color'] = convert_color(LAB, LCHabColor)
    
    # Производим перевод в RGB
    
    convert_dict['RGB_color'] = convert_color(LAB, AdobeRGBColor)

    # Производим перевод из RGB в HSV 
    convert_dict['HSV_color'] = convert_color(convert_dict['RGB_color'], HSVColor)
 
    # Производим перевод из RGB в HSL
    convert_dict['HSL_color'] = convert_color(convert_dict['RGB_color'], HSLColor)

    return(convert_dict)


# Функция для обратного перевода полученных значений в LAB
def convert_back_lab(convert_dict):
    
    # Создаем словарь, для удобного отображения результатов конвертирования
    back_convert_dict = {}

    # Производим перевод LCH в LAB
    back_convert_dict['LCH_LAB_color'] = convert_color(convert_dict['LCH_color'], LabColor)

    # Производим перевод RGB в LAB
    back_convert_dict['RGB_LAB_color'] = convert_color(convert_dict['RGB_color'], LabColor)

    # Производим перевод HSV в LAB
    HSV_RGB_color = convert_color(convert_dict['HSV_color'], AdobeRGBColor)
    back_convert_dict['HSV_LAB_color'] = convert_color(HSV_RGB_color, LabColor)

    # Производим перевод HSL в LAB
    HSL_RGB_color = convert_color(convert_dict['HSL_color'], AdobeRGBColor)
    back_convert_dict['HSL_LAB_color'] = convert_color(HSL_RGB_color, LabColor)
    
    return back_convert_dict


# Функция для вывода всех полученных значений
def print_convert_table(convert_from, convert_back):
    
    # Объединение словарей для единого вывода
    output_dict = convert_from | convert_back

    for key in output_dict.keys():
        output_dict[f'{key}'] = output_dict[f"{key}"].get_value_tuple()
        print(f'{key:15} | {output_dict[f"{key}"]}')

    # Расчёт показателей дельта Е
    delta_dict = {}
    
    for key in convert_back.keys():
        
        # Расчет дельта Е 
        delta_dict[f'delta_E - {key}'] = round(math.sqrt(
            (output_dict['LAB_color'][0] - output_dict[f'{key}'][0])**2 
            + (output_dict['LAB_color'][1] - output_dict[f'{key}'][1])**2 
            + (output_dict['LAB_color'][2] - output_dict[f'{key}'][2])**2), 3)

        # Расчет дельта Е94
        delta_dict[f'delta_E94 - {key}'] = round(delta_e_cie1994(convert_from['LAB_color'], convert_back[f'{key}']), 3)

        # Расчет дельта Е00
        delta_dict[f'delta_E00 - {key}'] = round(delta_e_cie2000(convert_from['LAB_color'], convert_back[f'{key}']), 3)

    for key in delta_dict.keys():
        print(f'{key:25} | {delta_dict[f"{key}"]}')


# Задаем изначальный цвет
LAB_color = LabColor(32, 22, -31)

convert_table_from = convert_from_lab(LAB_color)
convert_table_back = convert_back_lab(convert_table_from)

print_convert_table(convert_table_from, convert_table_back)