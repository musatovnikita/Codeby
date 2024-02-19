def get_input(prompt="Введите значение: ", data_type=int):
    try:
        user_input = input(prompt)
    except ValueError:
        print("Ошибка ввода!", f"Ввод пользователя должен быть {data_type}", sep="\n")
    else:
        print("Ввод успешен.")
        return data_type(user_input)