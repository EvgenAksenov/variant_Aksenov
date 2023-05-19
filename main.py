# Задаем кортеж из символов
t = ('a', 'b', 'c', 'd', 'd', 'e', 'f', 'f', 'f', 'g', 'h', 'i')

# Создаем словарь для подсчета частоты символов
char_freq = {}

# Проходим по каждому символу в кортеже
for char in t:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Выводим на экран частоту появления каждого символа
for char, freq in char_freq.items():
    print(char, freq)
