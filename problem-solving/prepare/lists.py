N = int(input())
arr = []
for i in range(N):
    command = input()
    if command.startswith("insert"):
        c, *arg = command.split()
        arr.insert(int(arg[0]), int(arg[1]))
    if command.startswith("print"):
        print(arr)
    if command.startswith("remove"):
        c, *arg = command.split()
        arr.remove(int(arg[0]))
    if command.startswith("append"):
        arg = command.split()[1]
        arr.append(int(arg))
    if command.startswith("sort"):
        arr = sorted(arr)
    if command.startswith("pop"):
        arr.pop()
    if command.startswith("reverse"):
        arr.reverse()