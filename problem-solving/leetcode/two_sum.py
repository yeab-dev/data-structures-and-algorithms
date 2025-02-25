from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List:
        numap = {}
        for index, number in enumerate(nums):
            dif = target - number
            if dif in numap:
                return [numap[dif], index]
            numap[number] = index
                 
    