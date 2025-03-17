import json

def vigenere_encrypt(text, key):
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

with open('old_text.txt', 'r', encoding='utf-8') as f:
    original_text = f.read()

with open('key.json', 'r', encoding='utf-8') as f:
    key = json.load(f)['key']

encrypted_text = vigenere_encrypt(original_text, key)

with open('new_text.txt', 'w', encoding='utf-8') as f:
    f.write(encrypted_text)
print("Готово. Зашифрованный текст в new_text.")