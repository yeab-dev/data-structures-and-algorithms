number = int(input())
binary = ""
reversed_binary = ""
reversed_decimal = 0
while not(number == 0):
    binary += str(number%2)
    number //= 2
for i in range(len(binary)-1, -1, -1):
    reversed_binary += str(binary[i])

for i in range (len(binary) -1, -1, -1):
    if(int(reversed_binary[i]) == 1):
        reversed_decimal += 2**i

print(reversed_decimal)