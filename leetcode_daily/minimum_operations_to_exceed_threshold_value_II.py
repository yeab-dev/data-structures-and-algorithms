import bisect
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        while len(nums) >= 2 and nums[0] < k:
            x = nums[0] * 2 + nums[1]
            nums.remove(nums[0])
            nums.remove(nums[0])
            bisect.insort(nums, x)
            count += 1

        return count