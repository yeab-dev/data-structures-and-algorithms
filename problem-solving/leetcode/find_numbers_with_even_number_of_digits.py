from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        validNumbers = 0
        for num in nums:
            if str(num).count() % 2 == 0:
                validNumbers += 1
        return validNumbers