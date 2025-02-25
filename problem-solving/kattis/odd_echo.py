num_of_words = int(input())

list_of_echos = []
for i in range(num_of_words):
    word = input()
    if (i % 2 == 0 ):
        list_of_echos.append(word)

for i in range(len(list_of_echos)):
    print(list_of_echos[i])

