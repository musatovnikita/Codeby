import re

text = '''Примеры расширений файлов: 
wald.jpeg 
wow.mp4 
book.txt 
forest.png 
fox.tiff 
wood.pdf 
hub.gif 
small.zip 
sound.mp3
'''

# Находим все строки с расширениями графических файлов
graphic_files = re.findall(r'\b\w+\.(?:jpeg|jpg|png|gif|tiff)\b', text, re.IGNORECASE)

# Выводим результат
for file in graphic_files:
    print(file)
