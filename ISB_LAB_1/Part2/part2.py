from collections import Counter

# 1. Частотный анализ текста
def frequency_analysis(text):
    text = text.replace('\n', '')
    total_chars = len(text)
    char_count = Counter(text)
    
    # Вычисляем вероятности
    probabilities = {char: count / total_chars for char, count in char_count.items()}
    return probabilities

# Чтение зашифрованного текста
with open('encrypted_code.txt', 'r', encoding='utf-8') as f:
    encrypted_text = f.read()

# Выполняем частотный анализ
probs = frequency_analysis(encrypted_text)

# Записываем вероятности в файл
with open('probabilities.txt', 'w', encoding='utf-8') as f:
    for char, prob in sorted(probs.items()):
        f.write(f'{char} = {prob:.6f}\n')

# 2. Чтение вероятностей алфавита
alphabet_probs = {}
with open('alphabet.txt', 'r', encoding='utf-8') as f:
    for line in f:
        char, prob = line.split(' = ')
        # Специальная обработка для пробела
        char = ' ' if char == '(пробел)' else char
        alphabet_probs[char] = float(prob)

# Сортируем вероятности для сопоставления
encrypted_probs_sorted = sorted(probs.items(), key=lambda x: x[1], reverse=True)
alphabet_probs_sorted = sorted(alphabet_probs.items(), key=lambda x: x[1], reverse=True)

# Создаем словарь замены символов
substitution = {}
for i in range(min(len(encrypted_probs_sorted), len(alphabet_probs_sorted))):
    enc_char, _ = encrypted_probs_sorted[i]
    alpha_char, _ = alphabet_probs_sorted[i]
    substitution[enc_char] = alpha_char

# 3. Дешифровка текста
decrypted_text = ''
for char in encrypted_text:
    decrypted_text += substitution.get(char, char)  # Если символа нет в словаре, оставляем как есть

# Записываем дешифрованный текст
with open('preliminary_code.txt', 'w', encoding='utf-8') as f:
    f.write(decrypted_text)

print("Дешифровка завершена. Результат записан в preliminary_code.txt")