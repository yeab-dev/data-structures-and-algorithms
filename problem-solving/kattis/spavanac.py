time = input()
hours = int(time.split(" ")[0])
minutes = int(time.split(" ")[1])
new_minute = 0
new_hour = 0

if (minutes > 45):
    new_minute -= 45
    new_hour = hours
elif(minutes < 45):
    new_minute = 60 - 45 + minutes
    new_hour = hours - 1

print (new_hour, new_minute)