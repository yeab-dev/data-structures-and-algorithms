def swap_case(s):
    swapped_string = ""
    for c in s:
        if (c.isupper()):
            swapped_string += c.lower()
        else:
            swapped_string += c.upper()
    return swapped_string