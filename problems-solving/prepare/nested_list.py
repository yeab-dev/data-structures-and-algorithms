scores = {}
for i in range(int(input())):
    name = input()
    score = float(input())
    scores[name] = score

sorted_list = sorted(list({i for i in scores.values()}))
second_lowest= sorted_list[1]

same_values = {}
print(list(sorted_list))
for k, v in scores.items():
    for a, b in scores.items():
        if (v == b) and not(k == a) and v == second_lowest:
            same_values[k] = v

if second_lowest in same_values.values():
    for i in sorted(same_values.keys()):
        print(i)
else: 
    [print(k) for k, v in scores.items() if v == second_lowest]
            