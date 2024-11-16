from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[int]:
        nums = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                nums.append("FizzBuzz")
            elif i % 3 == 0:
                nums.append("Fizz")
            elif i % 5 == 0:
                nums.append("Buzz")
            else:
                nums.append(str(i))
        return nums