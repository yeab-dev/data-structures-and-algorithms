from typing import List
def quick_sort(nums:List[int]):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x < pivot]
    greater = [x for x in nums[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)