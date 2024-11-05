rooms = int(input())
teams = int(input())

remainder = teams % rooms

for i in range(rooms):
    for j in range(teams // rooms):
        print("*", end= "")
    if not(remainder == 0):
            print("*", end="")
            remainder -= 1
    print()