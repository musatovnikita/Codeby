import re

def get_data():
    try:
        return input("Введите пароль: ")
    except (KeyboardInterrupt, EOFError, UnboundLocalError):
        print("Выполнение программы было остановлено внешним фактором")
        return False

def is_password_meet_conditions(password):
    pattern = (
        r"^(?=.*[A-Z])"  # Пароль должен содержать хотя бы одну заглавную букву
        r"(?=.*[a-z])"  # Пароль должен содержать хотя бы одну строчную букву
        r"(?=.*\d)"  # Пароль должен содержать хотя бы одну цифру
        r"(?=.*_)"  # Пароль должен содержать символ подчеркивания
        r"[A-Za-z\d_]{8,20}$"  # Пароль должен быть длиной от 8 до 20 символов и содержать только буквы, цифры и символ подчеркивания
    )
    return re.match(pattern, password) is not None

if __name__ == "__main__":
    password = get_data()
    if password:
        print("Пароль принят!") if is_password_meet_conditions(password) else \
            print("Пароль не соответствует требованиям!")