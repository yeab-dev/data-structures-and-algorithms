from typing import List
class Solution:
    def singleNumber(self, nums:List[int])-> int:
        num_map = {}
        for num in nums:
            if not num in num_map.keys():
                num_map[num] = 1
            else:
                num_map[num] += 1
        return [k for k, v in num_map.items() if v == 1][0]
print(Solution().singleNumber([4,1,2,1,2]))