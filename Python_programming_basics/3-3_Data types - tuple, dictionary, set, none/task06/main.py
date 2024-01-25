target_dict = {'o': 3, 'd': 7, 'k': 5, 'w': 2, 'e': 6, 'g': 1, 'y': 4}

print(''.join(list(target_dict)[::2]))
print('Сумма значений словаря:', sum(target_dict.values()))
print('Отсортированный список значений словаря:', sorted(target_dict.values()))
print('Сумма тертьих значений словаря:', sum(list(target_dict.values())[::3]))