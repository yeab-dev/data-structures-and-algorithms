from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        addition = 0
        avg = 0.0
        while i < len(nums) - k+1:
            addition = sum(nums[i:i+k])
            if addition / k > avg:
                avg = addition / k
            i += 1
        return avg
print(Solution().findMaxAverage([-1], 1))