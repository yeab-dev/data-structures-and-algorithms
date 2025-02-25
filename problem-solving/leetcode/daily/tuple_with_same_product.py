from typing import List
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        tuples = {}
        total = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                p = nums[i] * nums[j]
                if not p in tuples:
                    tuples[p] = []
                    tuples[p].append([[nums[i], nums[j]]])
                else:
                    tuples[p] += [[nums[i], nums[j]]]
        for tup in tuples.values():
            total += len(tup) * (len(tup)-1) // 2
        return 8 * total