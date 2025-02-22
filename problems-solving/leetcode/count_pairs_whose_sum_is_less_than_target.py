from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int):
        left, right, count = 0, len(nums)-1, 0
        sortedNums = sorted(nums)
        while left < right:
            if sortedNums[left] + sortedNums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count