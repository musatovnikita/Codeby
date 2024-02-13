from pyfiglet import Figlet
import get_str_digital_style as get

f = Figlet()
f.setFont(font="digital")
print(f.renderText("Pentester"))

if __name__ == "__main__":
    print(get.get_str_digital_style(input("Введите текст: ")))