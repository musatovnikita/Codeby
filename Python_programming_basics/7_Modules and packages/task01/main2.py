import string
import random

# Создаем список символов верхнего и нижнего регистра английского алфавита и цифр
characters = list(string.ascii_letters + string.digits)

# Перемешиваем список символов
random.shuffle(characters)

# Выбираем первые 10 символов после перемешивания
random_characters = characters[:10]

# Выводим выбранные символы на экран
print("Список случайных 10 символов:", random_characters, sep="\n")