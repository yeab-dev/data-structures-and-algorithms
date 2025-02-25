class Solution:
    def add(self, num: str) -> int:
        sum = 0
        for char in num:
            sum += int(char)
        return sum
    def addDigits(self, num: int) -> int:
        strNum = self.add(str(num))
        while len(str(strNum)) > 1:
            strNum = str(self.add(str(strNum)))
        return strNum