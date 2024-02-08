def print_string_info(string):
    print("Символов в предложении: ", len(string))
    word_list = str(string).split()
    print("Слова в предложении: ", len(word_list))
    print("Сколько раз встречается каждый знак:")
    for num in sorted(set(string)):
        print(num, "-", string.count(num))


if __name__ == '__main__':
    print_string_info(input("Введите предложение: "))