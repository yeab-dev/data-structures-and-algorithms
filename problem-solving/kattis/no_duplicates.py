sentence = input()

words = sentence.split(sep= " ")

valid = True
for i in range(len(words)):
    a = words[i]
    for j in range(len(words)):
        b = words[j]
        if i == j:
            print(i, "skip", j)
            continue
        elif(a == b):
            valid = False

if not(valid):
    print("no")
if valid:
    print("yes")