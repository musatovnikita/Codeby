def read_existing_passwords(filename):
    try:
        with open(filename, "rb") as file:
            existing_passwords = set(line.strip() for line in file)
    except FileNotFoundError:
        existing_passwords = set()
    return existing_passwords

def write_passwords_to_file(passwords, filename):
    with open(filename, "ab+") as file:
        for password in passwords:
            file.write(password + b'\n')

def generate_variants(word):
    variants = [
        word.upper(),
        word.lower(),
        word.capitalize(),
        word.swapcase(),
        word[::-1],
        word + "1",
        "1" + word,
        "-" + word + "-",
        word + "_",
        "_" + word,
        word + "!",
        word[:-1],
        word[1:],
    ]
    return variants

def input_words(default="python"):
    existing_passwords = read_existing_passwords("passwords.txt")
    words_list = [default]
    try:
        while (word := input("Введите пароль: ").strip()):
            if word in existing_passwords:
                print(f"Пароль '{word}' уже присутствует в списке.")
                continue
            else:
                variants = generate_variants(word)
                new_passwords = [variant.encode('utf-8') for variant in variants if variant not in existing_passwords]
                if new_passwords:
                    write_passwords_to_file(new_passwords, "passwords.txt")
                    existing_passwords.update(new_passwords)
                    print("\n".join(variants))
                    print(f"Количество строк в файле: {len(existing_passwords)}")
                else:
                    print("Нет уникальных вариантов пароля для добавления.")
    except KeyboardInterrupt:
        print("Программа завершена.")

if __name__ == "__main__":
    input_words()
