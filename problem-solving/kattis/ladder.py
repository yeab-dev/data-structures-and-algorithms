import math
given = input()
values = given.split(" ")
height = int(values[0])
angle = int(values[1]) * (math.pi / 180)

length_of_the_ladder = height / math.sin(angle)
print(int(math.ceil(length_of_the_ladder)))