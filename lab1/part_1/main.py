from ..modules.read_write_function import read_file, write_to_file

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

    try:

        encrypted_text = crypt(text, replacement_dict)
        write_to_file(config['encrypted_text_output_file_path'], encrypted_text)
        print("Зашифрованный текст успешно записан")

        decrypted_text = decrypt(encrypted_text, replacement_dict)
        write_to_file(config['decrypted_text_output_file_path'], decrypted_text)
        print("Расшифрованный текст успешно записан")

    except Exception as error:
        print(f"Произошла ошибка: {error}")

if __name__ == "__main__":
    main()
