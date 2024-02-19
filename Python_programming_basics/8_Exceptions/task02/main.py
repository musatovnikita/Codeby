def user_input_division(input_1, input_2):
    try:
        result = input_1 / input_2
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    except ValueError:
        return "Такое деление невозможно!"
    except TypeError:
        return "Возникла какая-то ошибка!"
    else:
        return result


def main():
    var_1, var_2 = [int(input("Введите число: ")) for _ in range(2)]

    if isinstance(result := user_input_division(var_1, var_2), float):
        print(f"Результат деления равен {result}")
    else:
        print("На ноль делить нельзя!", f"Программа остановлена! Поделить"
                                        f" {var_1} на {var_2} нельзя!",
              sep="\n")

if __name__ == "__main__":
    main()