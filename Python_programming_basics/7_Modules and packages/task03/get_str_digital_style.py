def get_str_digital_style(text):
    length = len(text)
    s = "+-" * length + "+\n|"
    for sym in text:
        s += sym + "|"
    s += "\n" + "+-" * length + "+"
    return s