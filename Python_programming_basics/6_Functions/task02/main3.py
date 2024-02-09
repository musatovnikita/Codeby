def ammo_off_time(ammo_count):
    if ammo_count not in range(250, 10001):
        print('Введите число от 250 до 10000.')
    else:
        fire_seconds = ((ammo_count - 1) // 250) * 20 + ammo_count / 20

        print('Патроны закончатся через', fire_seconds, 'сек.')


ammo_off_time(int(input('Введите количество патронов: ')))