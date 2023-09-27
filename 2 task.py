word = input("Введите слово: ")

upper_pairs = 0
lower_pairs = 0
vowel_count = 0

for i in range(len(word) - 1):
    current_char = word[i]
    next_char = word[i + 1]

    if current_char.isupper() and next_char.isupper():
        upper_pairs += 1

    if current_char.islower() and next_char.islower():
        lower_pairs += 1

    if current_char.lower() in "ауоиэыяюеё":
        vowel_count += 1

if word[-1].lower() in "ауоиэыяюеё":
    vowel_count += 1

print("Пар верхнего регистра :", upper_pairs)
print("Пар нижнего регистра :", lower_pairs)
print("Количество гласных букв:", vowel_count)
