def square_of(*args):
    args_list = [int(num) for num in args[0]]
    if len(args_list) == 1:
        pi = 3.14
        print("Площадь круга:", round(pi * (args_list[0] / 2 ** 2), 2),
              "кв. м.")
    elif len(args_list) == 2:
        print("Площадь прямоугольника:", args_list[0] *
              args_list[1], "кв. м.")
    elif len(args_list) == 3:
        p = (args_list[0] + args_list[1] + args_list[2]) / 2
        square = round((p * (p - args_list[0]) * (p - args_list[1])
                        * (p - args_list[2])) ** 0.5, 2)
        print("Площадь треугольника:", square, "кв. м.")

if __name__ == "__main__":
    square_of(input("Введите аргументы: ").split())