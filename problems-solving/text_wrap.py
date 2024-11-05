def wrap(string, width):
    new_string = ""
    counter = 0
    for c in string:
        counter += 1
        new_string += c
        if counter == width:
            new_string += "\n"
            counter = 0
    return new_string