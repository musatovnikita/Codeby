jewels = ('золото', 'алмазы', 'серебро', 'сапфиры', 'бронза', 'рубины',
          'платина', 'изумруды', 'палладий', 'аметисты')

for number in range(2):
    for index, value in enumerate(jewels[number::2], 1):
        print(index, value)
    print()