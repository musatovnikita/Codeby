def count_lines_in_file(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


if __name__ == "__main__":
    print(f"Количество строк в файле: {count_lines_in_file("city.txt")}")