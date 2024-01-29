if (string := input("Введите строку: ")):
    if len(string) > 100:
        print("Количество символов не должно быть больше 100!")
    elif len(string) % 10 == 1 and len(string) != 11:
        print("В строке", len(string), "символ")
    elif len(string) % 10 in (2, 3, 4) and len(string) not in (12, 13, 14):
        print("В строке", len(string), "символа")
    else:
        print("В строке", len(string), "символов")