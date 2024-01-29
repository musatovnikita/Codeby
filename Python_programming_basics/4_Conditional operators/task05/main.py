if 0 <= (hours := int(input("Введите часы: "))) <= 23 and\
    0 <= (minutes := int(input("Введите минуты: "))) <= 59 and\
    0 <= (seconds := int(input("Введите секунды: "))) <= 59:
            hours = "0" + str(hours)
            minutes = "0" + str(minutes)
            seconds = "0" + str(seconds)
            print(hours[-2:], minutes[-2:], seconds[-2:], sep=":")
else:
    print("Введите числа для часов от 0 до 23, и для минут и секунд от 0 до 59")