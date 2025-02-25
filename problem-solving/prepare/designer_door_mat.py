m, n = input().split(" ")
n = int(n)
m = int(m)
one_side_dashes = n//2 -1
dot_dot_bar = 0
while(one_side_dashes >= 3):
    print(one_side_dashes * "-" + ".|" + (dot_dot_bar * "..|")  + dot_dot_bar * "..|" + "."+ one_side_dashes * "-")
    one_side_dashes -= 3
    dot_dot_bar += 1

print("-" * (n//2 - 3) + "WELCOME" + "-" * (n//2 -3))

one_side_dashes += 3
dot_dot_bar -= 1
while(one_side_dashes <= n//2-1):

    print(one_side_dashes * "-" + ".|" + (dot_dot_bar * "..|")  + dot_dot_bar * "..|" + "."+ one_side_dashes * "-")
    one_side_dashes += 3
    dot_dot_bar -= 1