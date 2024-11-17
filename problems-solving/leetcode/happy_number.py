class Solution:
    def convert(self,strNum: str) -> int:
        sum = 0
        for num in strNum:
            sum += int(num) ** 2
        return sum
    def isHappy(self, n: int) -> bool:
        seen = set()
        while not n in seen:
            if n == 1: return True
            seen.add(n)
            n = self.convert(str(n))
        return False