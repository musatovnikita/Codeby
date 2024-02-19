def get_input(prompt, data_type):
    while True:
        try:
            user_input = input(prompt)
            converted_input = data_type(user_input)
            return converted_input
        except ValueError:
            print("Ошибка ввода!", f"Ввод пользователя должен содержать "
                                  f"{type(int())}", sep="\n")