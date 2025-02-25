from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)

        return int(n * (n + 1) / 2 - total_sum)

        # THIS IS CHEATING THO :(
