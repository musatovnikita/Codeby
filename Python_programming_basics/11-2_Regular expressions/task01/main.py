import re

text = 'Сначала был адрес http://yandex.ru, потом стал https://yandex.ru. ' \
       'Гугл https://google.com имеет шире охват чем https://yandex.ru.'

res = re.findall(r'(https?://\w+\.\w{2,3})(?!.*\1)', text)
print('\n'.join(res))