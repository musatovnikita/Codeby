def get_input():
    while not (num := input("Введите число: ")).isdigit() or not 10 <= int(num) <= 20:
        print("Ошибка! Вы ввели не число или число не в диапазоне!")
    print("Работаем с числом", num if 10 <= int(num) <= 12 else "")
    return int(num)


if __name__ == "__main__":
    get_input()