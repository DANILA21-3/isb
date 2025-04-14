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

def write_to_file(file_path: str, text: str):
    """
    Функция записывает строковую переменную в текстовый файл
    :param file_path: Путь, в котором будет храниться файл
    :param text: Записываемый текст 
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")