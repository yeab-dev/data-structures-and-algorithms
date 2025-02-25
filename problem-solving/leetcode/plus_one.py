from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lastIndex = len(digits) - 1
        if digits[lastIndex] == 9:
            while digits[lastIndex] == 9:
                digits[lastIndex] = 0
                lastIndex -= 1
                if lastIndex == -1:
                    digits.insert(0, 1)
                    return digits
            digits[lastIndex] = digits[lastIndex] + 1
            return digits
        digits[lastIndex] = digits[lastIndex] + 1
        return digits