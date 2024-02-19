from custom_input import get_input
import random

def main():
    user_input = None
    user_input = get_input("Введите число от 1 до 10: ", int)
    if not 1 <= user_input <= 10:
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

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Произошла критическая ошибка: {e}")