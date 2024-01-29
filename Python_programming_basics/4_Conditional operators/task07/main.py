time = input("Введите время: ").split(":")
hours, minutes = int(time[0]), int(time[1])

if (hours >= 18 and minutes > 0) or hours < 6:
    print("Солнце за горизонтом!")
else:
    degree = ((hours - 6) * 60 + minutes) * 0.25
    print("Угол солнца:", degree, "градусов")