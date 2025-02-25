
S = input()

def refactor(string):
    for c in string:
        if c.islower():
            return ord(c)
        if c.isupper():
            return ord(c) * 100_000
        if c.isdecimal:
            if int(c) % 2 != 0:
                return ord(c) * 100_000_000
            else:
                return ord(c) * 100_000_000_000
print(*sorted(S, key=refactor), sep="")