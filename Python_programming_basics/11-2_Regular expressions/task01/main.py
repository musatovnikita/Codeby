import re

text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru. Гугл https://google.com имеет шире охват чем https://yandex.ru.'

# Находим все URL в тексте, не захватывая точки и запятые в конце
urls = re.findall(r'https?://\S+(?<![.,])', text)

# Удаляем дубликаты
unique_urls = list(set(urls))

# Выводим результат
for url in unique_urls:
    print(url)