import json
from typing import Union

def read_file(file_path: str, file_type: str = 'json') -> Union[dict, str]:
    """
    Функция читает файл и возвращает его содержимое

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
            case 'bin':
                with open(file_path, 'rb') as file:
                    return file.read()
            case _:
                raise ValueError("Неподдерживаемый формат файла")
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return {} if file_type == 'json' else ""

def write_to_file(file_path: str, data: Union[str, dict], file_type: str):
    """
    Функция записывает данные в текстовый файл или JSON файл
    
    :param file_path: Путь, в котором будет храниться файл
    :param data: Записываемые данные
    :param file_type: Тип файла (txt или json)
    """
    try:
        match file_type:
            case 'json':
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, ensure_ascii=False, indent=1)
            case 'text':
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(data)
            case 'bin':
                with open(file_path, 'wb') as file:
                    file.write(data)
            case _:
                raise ValueError("Неподдерживаемый формат файла")
    except Exception as e:
        print(f"Ошибка при записи в файл {file_path}: {e}")

