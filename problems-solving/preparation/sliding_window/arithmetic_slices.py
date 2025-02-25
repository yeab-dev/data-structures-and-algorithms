from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        count = 0
        for start in range(n - 2):  
            diff = nums[start + 1] - nums[start]  

            for end in range(start + 2, n): 
                if nums[end] - nums[end - 1] == diff:
                    count += 1 
                else:
                    break 

        return count

