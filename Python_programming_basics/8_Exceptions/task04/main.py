from random import randint


try:
    number = int(input("Введите число от 1 до 10: "))
except ValueError as v:
    print("Вы ввели строку -", v)
else:
    if (random_number := randint(10, 100)) == number:
        print(number * 2)
    elif number in range(1, 11):
        print(sum(val for val in range(number, random_number + 1)))
    else:
        print('Введите число от 1 до 10')