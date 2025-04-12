import json
from typing import Union

def read_file(file_path: str, file_type: str = 'json') -> Union[dict, str]:
    """
    Читает файл и возвращает его содержимое.

    :param file_path: Путь к файлу
    :param file_type: Тип файла (txt или json)
    :return: Содержимое файла
    """
    try:
        match file_type:
            case 'json':
                with open(file_path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            case 'text':
                with open(file_path, 'r', encoding='utf-8') as file:
                    return file.read()
            case _:
                raise ValueError("Неподдерживаемый формат файла")
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return {} if file_type == 'json' else ""
    
def write_to_file(file_path: str, data: Union[str, dict], data_type: str) -> None:
    """
    Функция записывает данные в файл одного из форматов (txt или json)

    :param file_path: Хранит в себе путь для хранения файла
    :param data: Данные, которые будут записаны в файл (текст или словарь)
    :param data_type: Формат файла
    """
    try:
        match data_type:
            case 'text':
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(data)
            case 'json':
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
            case _:
                raise ValueError("Неподдерживаемый тип данных для записи в файл")
    except Exception as e:
        print(f"Ошибка при записи в файл {file_path}: {e}")

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

def replace_symbol(text, replacement_dict)-> str:
    """
    Функция производит замену символов в тексте согласно словарю замен
    
    :param text: Исходный текст для применения замен
    :param replacement_dict: Словарь, содержащий в себе замены символов 

    :return: Текст с выполненными заменами
    """
    new_text = ''
    for char in text:
        if char in replacement_dict:
            new_text += replacement_dict[char] 
        else:
            new_text += char  
    return new_text

def result_replacement(statistics_probability: dict, custom_replacements: dict, frequency_dict: dict )-> dict:
    """
    Функция создаёт конечный словарь, хранящий в себе замены изначальных символов на конечных, которые образуют расшифрованный текст
    
    :param statistics_probability: Словарь, содержащий наиболее встречаемые символы в тексте согласно статистике. Представлено в виде "Буква : Вероятность встречи"
    :param custom_replacements: Словарь, содержащий ручные замены, полученные методом подбора
    :param frequency_dict: Словарь, содержащий вероятность встречи символов в данном тексте

    :return: Конечный словарь, содержащий замены, которые приведут к расшифрованному тексту
    """

    replacement_dict = {}

    min_length = min(len(frequency_dict), len(statistics_probability))

    for i, symbol in enumerate(frequency_dict.keys()):
        if i < min_length:
            replacement_dict[symbol] = list(statistics_probability.keys())[i]

    replacement_dict.update(custom_replacements)

    return replacement_dict


def print_replacements(replacement_dict: dict) -> None:
    """
    Функция выводит в командную строку словарь, хранящий в себе замены, которые приведут зашифрованный текст к расшифрованному

    :param replacement_dict: Конечный словарь, содержащий замены, которые приведут к расшифрованному тексту
    """
    for original, replacement in replacement_dict.items():
            print(f"{original} -> {replacement}")

def main():
    config = read_file('config.json', 'json')

    statistics_probability = read_file(config['statistics_probability'], 'json')
    custom_replacements = read_file(config['custom_replacements'], 'json')
    text = read_file(config['input_text'], 'text')

    if text:
        frequency_dict = probability_symbol(text)
        print(frequency_dict)
        write_to_file(config['frequency_dict'], frequency_dict, 'json')

        replacement_dict = result_replacement(statistics_probability, custom_replacements, frequency_dict)
        print_replacements(replacement_dict)

        result_text = replace_symbol(text, replacement_dict)
        write_to_file(config['result_text'], result_text, 'text' )
        
    else:
        print("Текстовый файл пуст")

if __name__ == "__main__":
    main()
