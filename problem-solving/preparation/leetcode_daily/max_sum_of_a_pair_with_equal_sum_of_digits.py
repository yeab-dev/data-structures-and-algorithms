import heapq
from typing import List
from typing import Dict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map: Dict[int: List[int]] = {}
        valid_maxs = []
        for num in nums:
            digits = list(str(num))
            digits_sum = 0
            for i in range(len(digits)):
                digits_sum += int(digits[i])
            
            if digits_sum in digit_sum_map:
                digit_sum_map[digits_sum].append(num)
            else:
                digit_sum_map[digits_sum] = [num]

        for maxs in digit_sum_map.values():
            sorted_maxs = sorted(maxs)
            if len(sorted_maxs) < 2:
                continue
            else:
                valid_maxs.append(sorted_maxs[-1] + sorted_maxs[-2])
        if valid_maxs == []:
            return -1
        return max(valid_maxs)
