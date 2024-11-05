force_user = input()
a = int(input())
b = int(input())
difference = int(input())

if(abs(a - b) == -difference):
    print("JEDI")
elif(abs(a - b) == difference):
    if(a < b):
        print("SITH")
    elif(a > b):
        print("VEIT EKKI")