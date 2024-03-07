import re

def read_all_names():
    with open("surnames.txt", "r") as file:
        return file.read().split("\n")

def is_women_name(string):
    # Проверяем, оканчивается ли строка на "ВА", "НА" или "АЯ" с помощью регулярного выражения
    return re.search(r'(?:[ВН]А|АЯ)$', string, re.IGNORECASE) is not None

def write_to_file(file_name, line):
    with open(file_name, "a") as file:
        file.write(line + "\n")

def format_name(line):
    return line.lower().title()

if __name__ == "__main__":
    name_list = read_all_names()
    with open("woman.txt", "a") as woman_file, open("man.txt", "a") as man_file:
        for name in name_list:
            formatted_name = format_name(name)
            if is_women_name(formatted_name):
                woman_file.write(formatted_name + "\n")
            else:
                man_file.write(formatted_name + "\n")
    print("Done!")