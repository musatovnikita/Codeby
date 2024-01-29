if set(string_one := input("Введите первое слово: \n")) ==\
    set(string_two := input("Введите второе слово: \n")):
    print("Слова", string_one, "и", string_two, ("состоят из одних и "
                                                        "тех же букв."))
else:
    print("Введённые слова содержат различный набор букв.")