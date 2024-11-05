from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while len(nums) -1 > i:
            if not nums[i] == nums[j]:
                i += 1
                j += 1
            else:
                nums.remove(nums[j])
        return j