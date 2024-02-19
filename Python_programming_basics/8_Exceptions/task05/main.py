import random
from animals import *

def check_legal_value():
    try:
        number = int(input('Введите номер рисунка: '))
    except(ValueError, EOFError):
        return False
    else:
        if 1 <= number <= 7:
            return number


def choice_help():
    print('Help:\n')
    for key, (val, name) in animals_dict.items():
        print('\t' + str(key) + ')', name)
    print_animals()


def print_animals():
    if target_pic := check_legal_value():
        if target_pic == 7:
            target_pic = random.choice(sorted(animals_dict.keys())[:-1])
        print(animals_dict[target_pic][0])
    else:
        print('Введите число от 1 до 7.')


if __name__ == '__main__':
    animals_dict = {1: (deer, 'deer'), 2: (cat, 'cat'), 3: (cow, 'cow'),
                    4: (frog, 'frog'), 5: (bat, 'bat'),
                    6: (butterfly, 'butterfly'), 7: ('', 'random')}

    choice_help()