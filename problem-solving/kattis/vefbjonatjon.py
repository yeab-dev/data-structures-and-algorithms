num_of_servers = int(input())
parts_present = ""

CPU = 0
MEMORY = 0 
HD = 0
for i in range(num_of_servers):
    parts_present = input()
    item = parts_present.split(" ")
    if(item[0] == "J"):
        CPU += 1
    if(item[1] == "J"):
        MEMORY += 1
    if(item[2] == "J"):
        HD += 1

print(min(HD, CPU, MEMORY))