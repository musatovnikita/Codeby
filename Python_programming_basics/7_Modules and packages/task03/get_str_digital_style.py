def printing(text):
    first_line = "+-"*len(text) + "+"
    second_line = text.replace("", "|")
    return "\n".join((first_line, second_line, first_line))