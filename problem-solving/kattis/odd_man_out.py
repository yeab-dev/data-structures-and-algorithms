inputCount = int(input())
invitation_codes = []
for i in range(inputCount):
    num_of_guests = int(input())
    temp_codes = input()
    new_temps = temp_codes.split(" ")
    for temp in new_temps:
        if not(temp in invitation_codes):
            invitation_codes.append(temp)
        elif(temp in invitation_codes):
            invitation_codes.remove(temp)
    if not(len(invitation_codes) == 0):
        print("Case #", i+1, ": ", invitation_codes[0], sep="")
    invitation_codes = []