import argparse
import sys

from read_write_function import read_file, write_to_file
from sym import *
from asym import *

def generation_mode(enc_key_path: str, length_key: int, 
                    enc_nonce_path: str, length_nonce: int, 
                    public_key_path: str, private_key_path: str):
    """
    Функция генерирует ключ и параметр для симитричного шифрования.
    
    Также генерирует приватный и публичный ключ. 

    Параметр и ключ шифруются по публичному ключу и записываются в файл

    :param enc_key_path: путь для хранения зашифрованного ключа
    :param length_key: длина ключа
    :param enc_nonce_path: путь для хранения зашифрованного параметра, который используется в алгоритме симметричного шифрования
    :param length_nonce: длина параметра
    :param public_key_path: публичный ключ 
    :param private_key_path: приватный ключ
    """
    sym_key, nonce = generate_key_and_nonce(length_key,length_nonce)
    
    private_key, public_key = generate_assymetric_key()
    serialization_public_key(public_key, public_key_path)
    serialization_private_key(private_key, private_key_path)
    
    encrypted_sym_key = crypt_key_or_nonce(public_key, sym_key)
    nonce = crypt_key_or_nonce(public_key,nonce)
    serialization_key(encrypted_sym_key,enc_key_path)
    serialization_key(nonce, enc_nonce_path)
    
    print(f"Ключи успешно сгенерированы и сохранены:")
    print(f"- Зашифрованный симметричный ключ: {enc_key_path}")
    print(f"- Открытый ключ: {public_key_path}")
    print(f"- Закрытый ключ: {private_key_path}")
    print(f"- Nonce: {enc_nonce_path}")

def encryption_mode(input_file: str, priv_key_path: str, enc_key_path: str, enc_nonce_path:str, output_file: str):
    """
    Функция получает расшифрованный ключ и параметр, с помощью которых шифрует текст

    :param input_file: шифруемый текст
    :param priv_key_path: путь к приватному ключу
    :param enc_key_path: зашифрованный сим ключ
    :param output_file: зашифрованный текст
    """
    plaintext = read_file(input_file, 'text')
    private_key = deserialization_private_key(priv_key_path)
    encrypted_sym_key = read_file(enc_key_path, 'bin')
    encrypted_nonce = read_file(enc_nonce_path, 'bin')
    
    sym_key = decrypt_key(private_key, encrypted_sym_key)
    nonce = decrypt_key(private_key, encrypted_nonce)
    
    ciphertext = crypt_text(sym_key, nonce, plaintext)
    
    write_to_file(output_file, ciphertext, 'bin')
    print(f"Файл успешно зашифрован и сохранен в {output_file}")

def decryption_mode(input_file: str, priv_key_path: str, enc_key_path: str, enc_nonce_path: str, output_file: str):
    """
    Функция получает расшифрованный ключ, с помощью которого преобразует из зашифрованного текста расшифрованный

    :param input_file: зашифрованный текст
    :param priv_key_path: путь к приватному ключу
    :param enc_key_path: зашифрованный сим ключ
    :param output_file: расшифрованный текст
    """
    private_key = deserialization_private_key(priv_key_path)
    encrypted_sym_key = read_file(enc_key_path, 'bin')
    encrypted_nonce = read_file(enc_nonce_path, 'bin')
    ciphertext = read_file(input_file, 'bin')

    sym_key = decrypt_key(private_key, encrypted_sym_key)
    nonce = decrypt_key(private_key, encrypted_nonce)
    plaintext = decrypt_text(sym_key, nonce, ciphertext)

    write_to_file(plaintext, 'text')
    print(f"Файл успешно дешифрован и сохранен в {output_file}")

def main(): 
    try:
        cfg = read_file('config.json','json')
        config = cfg["Paths"]
        config_length = cfg["lengths"]
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required = True)
        group.add_argument('-gen', '--generation', action='store_true', help='Запускает режим генерации ключей')
        group.add_argument('-enc','--encryption', action='store_true', help='Запускает режим шифрования')
        group.add_argument('-dec','--decryption',action='store_true', help='Запускает режим дешифрования')
        
        args = parser.parse_args()
        
        if args.generation:
            generation_mode(config["enc_key_path"], 
                            config_length["length_key"], 
                            config["enc_nonce_path"], 
                            config_length["length_nonce"], 
                            config["public_key_path"], 
                            config["private_key_path"])
        elif args.encryption:
            encryption_mode(config["input_text"], config["private_key_path"], config["enc_key_path"], config["enc_nonce_path"], config["enc_text"])
        elif args.decryption:
            decryption_mode(config["enc_text"], config["private_key_path"], config["enc_key_path"], config["enc_nonce_path"], config["check_text"])
    except Exception as e:
        print(f"Ошибка при выполнении кода: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
