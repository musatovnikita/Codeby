from pyfiglet import Figlet
from get_str_digital_style import printing

f = Figlet()
f.setFont(font="digital")
print(f.renderText("Pentester"))

if __name__ == "__main__":
    print(printing(input("Введите текст: ")))