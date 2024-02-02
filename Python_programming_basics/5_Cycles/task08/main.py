targets = "7 раз отмерь, 1 раз отрежь.;Не имей 100 рублей, а имей 100 друзей.;1 за всех и все за 1."

for targets in tuple(targets.split(";")):
    print(targets, sum([int(number) for number in targets[:-1].split() if
                    number.isdigit()]))