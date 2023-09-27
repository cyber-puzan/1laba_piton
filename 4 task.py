word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

word1 = word1.lower().replace(" ", "")
word2 = word2.lower().replace(" ", "")

if sorted(word1) == sorted(word2):
    print("Эти слова являются анаграммами.")
else:
    print("Эти слова не являются анаграммами.")
