time_str = input("Введите время: ")
time_list = time_str.split(":")
hours = int(time_list[0])
minutes = int(time_list[1])

if (hours >= 18 and minutes > 0) or hours < 6:
    print("Солнце за горизонтом!")
else:
    degree = ((hours - 6) * 60 + minutes) * 0.25
    print("Угол солнца:", degree, "градусов")