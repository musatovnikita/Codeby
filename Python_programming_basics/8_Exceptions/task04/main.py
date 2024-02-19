from custom_input import get_input
import random

def main():
    try:
        user_input = get_input("Введите число от 1 до 10: ", int)
        if user_input < 1 or user_input > 10:
            print("Введите число от 1 до 10.")
            return

        random_number = random.randint(10, 100)
        print("Случайное число:", random_number)

        start_number = min(user_input, random_number)
        end_number = max(user_input, random_number)

        total_sum = sum(range(start_number, end_number + 1))

        print(f"Сумма чисел от {start_number} до {end_number}: {total_sum}")

        if user_input == random_number:
            print("Введенное число совпадает со случайным числом.")
            return total_sum  # Вернуть сумму чисел в случае совпадения.

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    return None  # Если совпадений нет или возникла ошибка, вернуть None.

if __name__ == "__main__":
    main()