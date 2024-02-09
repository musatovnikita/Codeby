def input_words(default="python"):
    words_list = [default]
    while (word := input("Введите любое слово: ")):
        if word in words_list:
            print("Строка ", word, " уже присутствует в списке на позиции ",
                  words_list.index(word) + 1)
            break
        words_list.append(word)
    print(words_list)

input_words()