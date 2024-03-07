import re

# Функция для чтения файла и извлечения уникальных логинов, доменов и паролей
def extract_credentials(file_name):
    with open(file_name, "r") as file:
        data = file.read()

    # Регулярное выражение для извлечения уникальных логинов, доменов и паролей
    pattern = r'(\b\w+@\w+\b)|(\b\w+://\w+\b)|(\b\w{8,}\b)'

    # Извлекаем уникальные логины, домены и пароли
    unique_credentials = re.findall(pattern, data)

    # Возвращаем уникальные логины, домены и пароли
    return unique_credentials

# Функция для записи уникальных объектов в файл
def write_to_file(file_name, data):
    with open(file_name, "w") as file:
        for item in data:
            file.write(item + "\n")

# Извлекаем уникальные логины, домены и пароли
unique_credentials = extract_credentials("base.txt")

# Подсчитываем количество уникальных логинов, доменов и паролей
unique_logins = len(set([login[0] for login in unique_credentials if login[0]]))
unique_domains = len(set([domain[1] for domain in unique_credentials if domain[1]]))
unique_passwords = len(set([password[2] for password in unique_credentials if password[2]]))

# Выводим количество найденных объектов
print("Логинов:", unique_logins)
print("Доменов:", unique_domains)
print("Паролей:", unique_passwords)