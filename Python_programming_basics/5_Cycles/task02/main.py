languages = "Python Golang PHP C# Java"

list_plus = [number_plus for number_plus in range(2, 51, 4)]
list_minus = [number_minus for number_minus in range(100, 66, -3)]
languages_dict = {value: value[0] for item, value in enumerate(
    languages.split())}

print(list_plus, list_minus, languages_dict, sep="\n")