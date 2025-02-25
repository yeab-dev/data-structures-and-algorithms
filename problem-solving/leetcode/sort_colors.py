from typing import List
class Solution:
    def sortColors(self, nums:List[int]) -> None:
        low,mid,high = 0,0,len(nums) - 1
        while mid <= high:
            if nums[mid] == 2:
                nums[mid],nums[high] = nums[high], nums[mid]
                high -= 1
            elif nums[mid] == 1:
                mid += 1
            
            elif nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
        print(nums)
Solution().sortColors([2,0,1])
