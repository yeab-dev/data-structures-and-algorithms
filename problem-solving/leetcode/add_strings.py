class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        result = []
        while i >= 0 or j >= 0:
            if i < 0:
                addition = str(int(num2[j]) + carry)
            elif j < 0:
                addition = str(int(num1[i]) + carry)
            else: addition = str(int(num1[i]) + int(num2[j]) + carry)
            if len(addition) > 1:
                carry = 1
                result.insert(0, addition[-1])
            else:
                result.insert(0, addition)
                carry = 0
            i -= 1
            j -= 1
        if carry >= 1:
            result.insert(0, str(carry))
        return "".join(result)