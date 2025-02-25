from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        countMap = {} 
        for num in nums:
            countMap[num] = True
        
        return [n for n in range(1, len(nums) +1) if not n in countMap]