n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

sum = 0.0
average = 0.0
for name, value in student_marks.items():
    if(name == query_name):
        for score in value:
            sum += score
        average = sum / 3

print("{:.2f}".format(average))