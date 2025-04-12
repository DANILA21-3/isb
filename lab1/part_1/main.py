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
    Фунция записывает строковую переменную в текстовый файл

    :param file_path: Путь, в котором будет храниться файл
    :param text: Записываемый текст 
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")

def crypt(text: str, replacement_dict: dict):
    """
    Фунция шифрует текст согласно словарю замен

    :param text: Шифруемый текст
    :param replacement_dict: Словарь замен

    :return: Зашифрованный текст
    """
    up_text = text.upper()
    new_text = ''
    for char in up_text:
        if char in replacement_dict:
            new_text += replacement_dict[char] 
        else:
            new_text += char  
    return new_text

def decrypt(encrypted_text: str, replacement_dict: dict):
    """
    Дешифрует текст по заданному словарю замен
    
    :param encrypted_text: Зашифрованный текст
    :param replacement_dict: Словарь замен, которые использовались при шифровании

    :return: Расшифрованный текст
    """

    reverse_dict = {v: k for k, v in replacement_dict.items()}
    original_text = ''
    for char in encrypted_text:
        if char in reverse_dict:
            original_text += reverse_dict[char] 
        else:
            original_text += char  
    return original_text

def main():

    config = read_file('config.json', 'json')

    text = read_file(config['input_file_path'], 'text')
    replacement_dict = read_file(config['requirements_file_path'], 'json')

    if text:

        encrypted_text = crypt(text, replacement_dict)
        write_to_file(config['encrypted_text_output_file_path'], encrypted_text)
        print("Зашифрованный текст успешно записан")

        decrypted_text = decrypt(encrypted_text, replacement_dict)
        write_to_file(config['decrypted_text_output_file_path'], decrypted_text)
        print("Расшифрованный текст успешно записан")

    else:
        print("Текст для шифрования пуст")

if __name__ == "__main__":
    main()
