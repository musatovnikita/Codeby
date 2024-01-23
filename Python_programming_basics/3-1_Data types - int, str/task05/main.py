var_1, var_2, var_3 = 29, 138, 7005

str_1, str_2, str_3 = str(var_1), str(var_2), str(var_3)
str_1, str_2, str_3 = str_1[1:2:1], str_2[1:2:1], str_3[0:1:1]

num_1, num_2, num_3 = var_1%10, var_2%100//10, round(var_3//100/10)

print("Число", "Через строку", "Через деление", sep="\t")
print(var_1, "\t\t", str_1, "\t\t\t\t", num_1)
print(var_2, "\t", str_2, "\t\t\t\t", num_2)
print(var_3, "\t", str_3, "\t\t\t\t", num_3)