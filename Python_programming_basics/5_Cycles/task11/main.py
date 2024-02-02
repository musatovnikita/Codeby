number = int(input("Введите любое число от 0 до 30: "))
for num in range(0, 20, 2):
    print(num)
    if number == num:
        print("Аварийно завершили цикл.", "Вышли из цикла!", sep="\n\n")
        break
else:
    print("Число пользователя = ", number)
    print("При переборе не попалось!", "Вышли из цикла!", sep="\n\n")