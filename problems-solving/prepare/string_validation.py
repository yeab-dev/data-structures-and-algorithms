def validate(s, validator):
    if(validator == "digit"):
        for c in s:
            if(c.isdigit()):
                return True
    if(validator == "lower"):
        for c in s:
            if(c.islower()):
                return True
    if(validator == "upper"):
        for c in s:
            if(c.isupper()):
                return True
    if(validator == "alpha"):
        for c in s:
            if(c.isalpha()):
                return True
    if(validator == "alphanum"):
        for c in s:
            if(c.isalnum()):
                return True

s = input()
if not validate(s, "alphanum"):
    print(False)
else:
    print(True)
if not (validate(s, "alpha")):
    print(False)
else:
    print(True)
if not validate(s, "digit"):
    print(False)
else:
    print(True)
if validate(s, "lower"):
   print(True)
else:
    print(False)
if validate(s, "upper"):
    print(True)
else:
    print(False)
    