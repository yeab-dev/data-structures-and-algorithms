from typing import List
def quick_sort(nums:List[int]):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [x for x in nums[1:] if x < pivot]
    greater = [x for x in nums[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([213,334,54,32,1,54,67,78,9,87,5,34,32,231,54,67,8,988,3,3,213,32]))