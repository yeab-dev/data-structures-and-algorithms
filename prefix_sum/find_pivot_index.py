from typing import List
class Solution:
    def pivotIndex(self, nums:List[int]):
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        totalSum = sum(nums)

        
        for i in range (0, len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = totalSum - nums[i]
            else:
                left_sum = prefix_sum[i-1]
                right_sum = totalSum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
        
        return -1
