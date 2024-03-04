import re

def get_data():
    try:
        return input("Введите пароль: ")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Выполнение программы было остановлено внешним фактором")
        return False


def is_start_as_capital(string):
    return re.match(r"^[A-Z]", string) is not None


def is_contains_latin(string):
    return re.search(r"[a-zA-Z]", string) is not None


def is_contains_digits(string):
    return re.search(r"\d", string) is not None


def is_contains_underscore(string):
    return '_' in string


def is_string_end_correct(string):
    return re.match(r".*[a-zA-Z\d]$", string) is not None


def is_string_length_correct(string):
    return 8 <= len(string) <= 20


def is_password_meet_conditions(string):
    conditions = [
        is_start_as_capital(string),
        is_contains_latin(string),
        is_contains_digits(string),
        is_contains_underscore(string),
        is_string_end_correct(string),
        is_string_length_correct(string)
    ]
    return all(conditions)


if __name__ == "__main__":
    password = get_data()
    if password:
        print("Пароль принят!") if is_password_meet_conditions(password) else \
            print("Пароль не соответствует требованиям!")