questions = input()
nums = questions.split(";")
num_of_questions = 0

for i in range(len(nums)):
    if("-" in nums[i]):
        num = nums[i].split("-")
        num_of_questions += int(num[1]) - int(num[0]) + 1
    else:
        num_of_questions += 1
print(num_of_questions)