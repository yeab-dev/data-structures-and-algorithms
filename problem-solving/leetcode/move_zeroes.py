from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == 0:
                nums.insert(j, nums.pop(i))
                j -= 1
            else: i += 1
        print(nums)