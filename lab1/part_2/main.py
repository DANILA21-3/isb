import json
from typing import Union

def probability_symbol(text: str) -> dict:
    """
    Функция используется для подсчёта вероятностей появления символов в заданном тексте

    :param text: текст, используемый для рассчёта вероятностей
    :return: отсортированный словарь с статистикой появления символов
    """
    symbols = set(text)
    result = {}

    for symbol in symbols:
        if symbol == '\n':
            continue
        count_symbol = text.count(symbol)
        probability = count_symbol / len(text)
        result[symbol] = probability

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    return sorted_result

def read_file(file_path: str, file_type: str = 'json') -> Union[dict, str]:
    """
    Читает файл и возвращает его содержимое

    :param file_path: Путь к файлу
    :param file_type: Тип файла( txt или json )
    :return: Содержимое файла 
    """
    try:
        if file_type == 'json':
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        elif file_type == 'text':
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        else:
            raise ValueError("Неподдерживаемый формат файла")
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return {} if file_type == 'json' else ""

statistics_probability = read_file('statistics_probability.json', 'json')

custom_replacements = read_file('custom_replacements.json', 'json')

text = read_file('cod23.txt', 'text')

if text:
    frequency_dict = probability_symbol(text)

    print(frequency_dict)

    replacement_dict = {}
    min_length = min(len(frequency_dict), len(statistics_probability))

    for i, symbol in enumerate(frequency_dict.keys()):
        if i < min_length:
            replacement_dict[symbol] = list(statistics_probability.keys())[i]

    replacement_dict.update(custom_replacements)

    new_text = ''
    for char in text:
        new_text += replacement_dict.get(char, char)  

    for original, replacement in replacement_dict.items():
        print(f"{original} -> {replacement}")

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(new_text)
else:
    print("Текстовый файл пуст")
