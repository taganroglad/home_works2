import string

# Чтение файла "war_and_peace.txt"
with open('war_and_peace.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Статистика по буквам и символам
total_chars = len(text)
char_stats = {}
for char in text:
    if char in string.printable and char not in string.ascii_letters:
        if char in char_stats:
            char_stats[char] += 1
        else:
            char_stats[char] = 1

# Вывод статистики
print("Статистика:")
for char, count in char_stats.items():
    print(f"{char} : {count / total_chars:.2f}")

# Поиск предложений с именем "Андрей"
sentences = text.split('. ')
andre_sentences = []
for sentence in sentences:
    if 'Андре' in sentence:
        andre_sentences.append(sentence.strip())

# Вывод 10 предложений с именем "Андрей"
print("\nПредложения со словом «Андрей»:")
for i, sentence in enumerate(andre_sentences[:10]):
    print(sentence)
