from typing import List
from random import Random
def quick_sort(nums:List[int]):
    if len(nums) < 2:
        return nums
    pivot = nums[Random().randint(0, len(nums) - 1)] 
    left = [x for x in nums if x < pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)