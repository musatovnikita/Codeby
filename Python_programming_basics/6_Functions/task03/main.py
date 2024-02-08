word = input("Введите слово: ")
result = lambda new_word: "Это слово больше, чем predator" \
    if new_word > "predator" else "Это слово меньше, чем predator"

print(result(word))