import json

def vigenere_encrypt(text: str, key: str) -> str:
    """
    Шифруем текст шифром Виженера.

    :param text: Исходный текст для шифрования.
    :param key: Ключ шифрования.
    :return: Зашифрованный текст.
    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ''
    key = key.lower()
    key_index = 0

    for char in text.lower():
        if char in alphabet:
            char_pos = alphabet.index(char)
            key_char = key[key_index % len(key)]
            key_pos = alphabet.index(key_char)
            new_pos = (char_pos + key_pos) % len(alphabet)
            encrypted_text += alphabet[new_pos]
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def read_text_from_file(file_path: str) -> str:
    """
    Текст из файла.

    :param file_path: Путь к файлу.
    :return: Текст файла.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_key_from_json(file_path: str) -> str:
    """
    Ключ из JSON.

    :param file_path: Путь к JSON файлу.
    :return: Ключ шифрования.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)['key']

def write_text_to_file(file_path: str, text: str) -> None:
    """
    Зашифрованный текст.

    :param file_path: Путь к файлу.
    :param text: Зашифрованный текст.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
        
original_text = read_text_from_file('old_text.txt')
key = read_key_from_json('key.json')
encrypted_text = vigenere_encrypt(original_text, key)
write_text_to_file('new_text.txt', encrypted_text)
print("Готово. Зашифрованный текст в new_text.")
