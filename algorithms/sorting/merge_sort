from typing import List
def merge_sort(nums: List[int]):
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = nums.copy()[:middle]
    right = nums.copy()[middle:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left: List[int], right: List[int]):
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged