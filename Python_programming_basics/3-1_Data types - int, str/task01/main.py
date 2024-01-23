language = "Языки программирования: Pyp, Python, Goland, Jaba..."

print(language[:24] + language[24:-2].upper().replace("PYP",
                                                         "PHP").replace(
    "GOLAND", "GOLANG").replace("JABA", "JAVA"))
