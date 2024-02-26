import time


def filter_cities_by_first_and_last_letter(first_letter, last_letter):
    filtered_cities = []
    with open("city.txt", "r") as file:
        for line in file:
            city = line.strip()
            if city[0] == first_letter and city[-1] == last_letter:
                filtered_cities.append(city)
    return filtered_cities


def write_to_file(data):
    timestamp = time.strftime("%m-%d_%H-%M-%S")
    filename = f"results_{timestamp}.txt"
    with open(filename, "w") as file:
        for city in data:
            file.write(city + "\n")
    print(f"Записали данные в файл: {filename}")


if __name__ == "__main__":
    first_letter, last_letter = input(
        "Введите первую и последнюю букву: ").strip().capitalize().split()

    filtered_cities = filter_cities_by_first_and_last_letter(first_letter,
                                                             last_letter)

    if filtered_cities:
        print("Список городов:")
        for city in filtered_cities:
            print(city)

        write_file = input(
            "Записать данные в файл? (д/н): ").strip().lower()
        if write_file == "д":
            write_to_file(filtered_cities)
    else:
        print("Нет городов, соответствующих заданным условиям.")