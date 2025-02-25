from typing import List
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        minimum = min(prefix_sum)

        return max(1, 1 - minimum)