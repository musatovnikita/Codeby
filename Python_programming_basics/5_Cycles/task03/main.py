targets = ('192.168.0.1', '10.10.1.1', '127.0.0.1')
ports = (80, 8080, 22)

# Первый вариант решения
dictionary = dict(zip(targets, ports))
print("Первый вариант решения")
for ip, port in dictionary.items():
    print(ip, port, sep="\t\t\t")

# Второй вариант решения
print()
print("Второй вариант решения")
for var_1, var_2 in zip(targets, ports):
    print(var_1, var_2, sep="\t\t\t")