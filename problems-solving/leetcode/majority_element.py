from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if not num in numMap:
                numMap[num] = 1
            elif numMap[num] >= len(nums)//2:
                return num
            else: numMap[num] += 1