from typing import List, Dict
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        currentSum, maxSum = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] >  nums[i-1]:
                currentSum += nums[i]
            else:
                maxSum = max(maxSum, currentSum)
                currentSum = nums[i]

        return max(maxSum, currentSum)

        

print(Solution().maxAscendingSum([10,20,30,5,10,50]))