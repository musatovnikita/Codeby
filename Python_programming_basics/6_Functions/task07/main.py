def count_characters_with_spaces(sentence):
    return len(sentence)


def count_words(sentence):
    words = sentence.split()
    return len(words)


def count_character_frequency(sentence):
    char_frequency = {}
    for char in sentence:
        char_frequency[char] = char_frequency.get(char, 0) + 1
    return char_frequency


def main():
    user_sentence = input("Введите предложение: ")

    # Подсчет количества символов с пробелами
    char_count = count_characters_with_spaces(user_sentence)
    print("Символов в предложении: ", char_count)

    # Подсчет количества слов
    word_count = count_words(user_sentence)
    print("Слова в предложении: ", word_count)

    # Подсчет частоты встречаемости каждого символа
    char_frequency = count_character_frequency(user_sentence)
    sorted_char_frequency = sorted(char_frequency.items())
    print("Сколько раз встречается каждый знак:")
    for char, freq in sorted_char_frequency:
        print(char, " - ",  freq)


if __name__ == "__main__":
    main()