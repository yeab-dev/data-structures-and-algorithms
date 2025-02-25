inputs = input()
values = inputs.split(sep= " ")
n = int(values[0])
x = int(values[1])

sum = 0

for i in range(int(n)):
    num_of_sanitizers = int(input())
    sum += num_of_sanitizers

if (sum <= x):
    print("Jebb")
else:
    print("Neibb")