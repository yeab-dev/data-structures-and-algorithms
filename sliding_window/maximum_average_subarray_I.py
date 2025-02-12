from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        addition = sum(nums[:k])
        max_avg = addition / k 

        for i in range(k, len(nums)):
            addition += nums[i] - nums[i - k]
            max_avg = max(max_avg, addition / k)

        return max_avg