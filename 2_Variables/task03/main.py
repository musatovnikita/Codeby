rectangular_house = 7 * 9
round_house = 3.14 * 9**2 / 4
wrong_house = 3 + 1/2

if rectangular_house > round_house:
    print('В самом маленьком доме живёт Александра')
elif rectangular_house < round_house:
    print('В самом маленьком доме живёт Юрий')
elif round_house > wrong_house:
    print('В самом маленьком доме живёт Владимир')
elif round_house < wrong_house:
    print('В самом маленьком доме живёт Александра')
elif rectangular_house > wrong_house:
    print('В самом маленьком доме живёт Владимир')
elif rectangular_house < wrong_house:
    print('В самом маленьком доме живёт Юрий')