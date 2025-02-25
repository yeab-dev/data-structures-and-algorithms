first = int(input())
second = int(input())
third = int(input())

def minimum(first, second, third):
    if(first < second and first < third):
        return "Monnei"
    elif (second < first and second < third):
       return "Fjee"
    else:
        return "Dolladollabilljoll"

print(minimum(first, second, third))
    