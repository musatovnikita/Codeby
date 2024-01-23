price_car = 11000
bank = 25
expenditures = 15

# Вычисляем всю сумму заработка
total_amount = price_car*4

# Вычисляем, какую сумму положил в банк
total_bank = total_amount*bank/100

# Вычисляем, сколько потратил
total_spent = total_amount*expenditures/100

# Вычисляем, сколько потратил денег
spent_money = price_car + total_bank + total_spent

# Вычмсляем сколько осталось денег
answer = total_amount - spent_money

print('У Пети осталось', answer, '$ наличных')