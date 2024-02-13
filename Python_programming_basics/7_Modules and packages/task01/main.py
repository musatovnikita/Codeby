import random
import string

target_range = string.ascii_letters + string.digits

# Вариант 1. Используем randint. Самый худший вариант.
print("Список случайных 10 символов:", [target_range[random.randint(0,
                                                                    len(target_range) - 1)]
                                        for _ in range(10)], sep="\n")

# Вариант 2. Используем sample. В этом варианте точно не будет повторений.
print("Список случайных 10 символов:", random.sample(target_range, 10),
      sep="\n")

# Вариант 3. Используем choice
print("Список случайных 10 символов:", [random.choice(target_range) for _ in
                                        range(10)], sep="\n")

# Вариант 4. Используем choices - более продвинутая версия, где можно указать множество параметров
print("Список случайных 10 символов:", random.choices(target_range, k=10),
      sep="\n")