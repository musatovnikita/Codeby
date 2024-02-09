
def ammo_off_time(ammo_count):
    if ammo_count not in range(250, 10001):
        print('Введите число от 250 до 10000.')
        return False

    tapes_change_counts = ammo_count // 250
    if ammo_count % 250 == 0:
        tapes_change_counts -= 1

    tapes_change_seconds = tapes_change_counts * 20
    fire_seconds = ammo_count / (1200 / 60)  + tapes_change_seconds

    print('Патроны закончатся через', fire_seconds, 'сек.')

ammo_off_time(int(input('Введите количество патронов: ')))