class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1
        while x < num:
            x += (2*x + 1)
        return x == num