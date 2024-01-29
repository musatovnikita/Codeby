if (number := int(input("Введите возраст: "))):
    if number < 1 or number > 100:
        print("Введите число от 1 до 100")
    else:
        if 1 <= number <= 6:
            print("Детство это – прекрасно!")
        elif 7 <= number <= 17:
            print("Учиться, учиться, учиться...")
        elif 18 <= number <= 64:
            print("Теперь ты можешь делать всё что угодно!")
        elif 65 <= number <= 100:
            print("Заслуженный отдых")