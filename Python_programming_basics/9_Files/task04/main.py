def input_words(default="python"):
    words_list = [default]
    try:
        with open("passwords.txt", "a+") as file:
            while True:
                word = input("Введите пароль: ").strip()
                if word in words_list:
                    print(f"Пароль '{word}' уже присутствует в списке.")
                    continue
                else:
                    words_list.append(word)
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
                        # Дополнительные варианты записи
                        "_" + word,
                        word + "!",
                        word[:-1],  # Удаление последней буквы
                        word[1:],   # Удаление первой буквы
                    ]
                    for variant in variants:
                        if variant not in words_list:
                            words_list.append(variant)
                            file.write(variant + "\n")
                    print("\n".join(variants))
                    print(f"Количество строк в файле: {len(words_list)}")
    except KeyboardInterrupt:
        print("Программа завершена.")

input_words()
