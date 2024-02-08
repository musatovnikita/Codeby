def count_symbols(text):
    """Функция считает количество символов во входящей строке без учёта пробелов."""
    text = text.replace(" ", "")
    print("Количество символов в предложении: ", len(text))
    print(count_symbols.__doc__)

if __name__ == "__main__":
    count_symbols(input("Введите предложение: "))