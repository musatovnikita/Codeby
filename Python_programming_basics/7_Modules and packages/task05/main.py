import time
import random
from lorem_text import lorem
from colorama import Fore, Style

def generate_random_words():
    word_count = random.randint(5, 15)
    random_text = lorem.words(word_count)
    return random_text

def countdown():
    for i in range(3, 0, -1):
        print(i, end='... ')
        time.sleep(1)
    print(Fore.RED + "Начали!" + Style.RESET_ALL)

def calculate_speed(start_time, end_time, input_text):
    elapsed_time = end_time - start_time
    words_typed = len(input_text.split())
    speed = words_typed / (elapsed_time / 60)
    return elapsed_time, speed

def display_statistics(elapsed_time, speed):
    print(Fore.GREEN + "#"*36 + Style.RESET_ALL)
    print(Fore.GREEN + "###### Вы отлично справились! ######" + Style.RESET_ALL)
    print(Fore.GREEN + "###### Время печати: {:.2f} с. #######".format(elapsed_time) + Style.RESET_ALL)
    print(Fore.GREEN + "### Скорость печати: {:.2f} зн/м ####".format(speed) + Style.RESET_ALL)
    print(Fore.GREEN + "#" * 36 + Style.RESET_ALL)

def print_typing_error():
    print(Fore.LIGHTMAGENTA_EX + "Увы, в тесте вы допустили ошибки".center(
        34, " ") +
          Style.RESET_ALL)

def main():
    while True:
        countdown()
        random_text = generate_random_words()
        print()
        print(random_text.center(len(random_text) + 2, " "))
        print()
        start_time = time.time()
        typed_text = input("Введите текст выше: ")
        end_time = time.time()
        if typed_text == random_text:
            elapsed_time, speed = calculate_speed(start_time, end_time, typed_text)
            display_statistics(elapsed_time, speed)
        else:
            print_typing_error()
        choice = input("Начать заново(д) или завершить программу(н)?")
        if choice.lower() != "д":
            print("До новых встреч!")
            break

if __name__ == "__main__":
    main()