print('fanat > apple', 'fanat' > 'apple')
print('fanat > abracadabra', 'fanat' > 'abracadabra')
print('fanat > Tarantino', 'fanat' > 'Tarantino')
print('fanat > yahoo', 'fanat' > 'yahoo')
print('yahoo > yandex', 'yahoo' > 'yandex')
print('yandex > gool', 'yandex' > 'gool')
print('yandex > logo', 'yandex' > 'logo')
# В данной задаче проводится лексикографическое сравнение, а это значит,
# что мы сравниваем "вес" символа по его порядковому номеру из таблицы
# кодировок. В получившимся результате 'yandex' > 'logo', т.к. порядковый
# номер первого символа слова 'yandex' - 'y', выше чем порядковый номер
# первого символа второго слова 'logo' = 'l'. Если первые символы были равны,
# то сравнение перешло ко вторым символам и так далее.