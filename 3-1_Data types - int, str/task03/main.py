word_one = "ворон"
word_two = "киноник"
word_three = "ротатор"
word_four = "город"
word_five = "тартрат"
number_one = 721217
number_two = 123321

answer_one = word_one[::-1]
answer_two = word_two[::-1]
answer_three = word_three[::-1]
answer_four = word_four[::-1]
answer_five = word_five[::-1]
number_one_str = str(number_one)
answer_six = number_one_str[::-1]
number_two_str = str(number_two)
answer_seven = number_two_str[::-1]

print(word_one, answer_one, word_one == answer_one)
print(word_two, answer_two, word_two == answer_two)
print(word_three, answer_three, word_three == answer_three)
print(word_four, answer_four, word_four == answer_four)
print(word_five, answer_five, word_five == answer_five)
print(number_one_str, answer_six, number_one_str == answer_six)
print(number_two_str, answer_seven, number_two_str == answer_seven)
