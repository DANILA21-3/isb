import json

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        text = file.read()
except Exception as e:
    print(f"Ошибка: {e}")
    text = ""

try:
    with open('key.json', 'r', encoding='utf-8') as f:
        replacement_dict = json.load(f)
except Exception as e:
    print(f"Ошибка: {e}")
    replacement_dict = {}


up_text = text.upper()

new_text = ''
for char in up_text:
    if char in replacement_dict:
        new_text += replacement_dict[char] 
    else:
        new_text += char  

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(new_text)  

