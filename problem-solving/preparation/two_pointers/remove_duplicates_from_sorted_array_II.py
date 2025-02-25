from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, count = 0, 0, 0

        while j < len(nums) and nums[j] != "_":
            if nums[i] == nums[j]:
                j += 1
                count += 1
                if count > 2:
                    nums[i] = nums[j]
            else:
                i = j
                count = 0
        return len(nums[:j])
