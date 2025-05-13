from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import os

def generate_key_and_nonce(length_key:int, length_nonce:int):
    """
    Функия генерирует бинарные последовательности заданной длины

    :param length_key: длина ключа
    :param length_nonce: длина параметра

    :return key,nonce: сгенерированный ключ и параметр
    """
    key = os.urandom(length_key) 
    nonce = os.urandom(length_nonce)

    return key,nonce

def serialization_key(key : bytes, file_name : str):
    """
    Записывает ключ в файл

    :param key: сам ключ
    :param file_name: путь для записи
    """
    with open(file_name, 'wb') as key_file:
        key_file.write(key)

def serialization_nonce(nonce : bytes, file_name : str):
    """
    Записывает параметр в файл

    :param nonce: сам параметр
    :param file_name: путь для записи
    """
    with open(file_name, 'wb') as nonce_file:
        nonce_file.write(nonce)

def deserialization_key_or_nonce(file_path : str)->bytes:
    """
    Считывает ключ/параметр с файла

    :param file_name: путь для чтения

    :return data: значение ключа/параметра
    """
    with open(file_path, mode='rb') as key_file: 
        data = key_file.read()

    return data

def crypt_text(key: bytes, nonce: bytes, text: str) -> bytes:
    """
    Шифрует текст согласно заданному алгоритму шифрования

    :param key: ключ для шифрования
    :param nonce: параметр для шифрования
    :param text: текст для шифрования

    :return chipertext: зашифрованный текст
    """
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(text.encode('utf-8')) 
    return ciphertext

def decrypt_text(key: bytes, nonce: bytes, crypt_text: bytes) -> str:
    """
    Расшифровывает текст согласно заданному алгоритму шифрования

    :param key: ключ для расшифрования
    :param nonce: параметр для расшифрования
    :param text: текст для расшифрования

    :return result_text: расшифрованный текст
    """
    decipher = ChaCha20.new(key=key, nonce=nonce)
    decrypted_text = decipher.decrypt(crypt_text)
    result_text = decrypted_text.decode('utf-8')

    return result_text

    