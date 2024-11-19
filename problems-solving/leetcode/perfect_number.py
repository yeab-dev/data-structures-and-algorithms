from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sum = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                sum += i
                if i != num // i:
                    sum += num // i
        return sum == num
