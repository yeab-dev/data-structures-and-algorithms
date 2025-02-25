def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)

x = "Hello there"
print(mutate_string(x, 3, "x"))