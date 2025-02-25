from typing import List
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_count = {}
    
        for i in range(len(nums)):
            diff = i - nums[i]

            good_pairs_count = diff_count.get(diff, 0)
            bad_pairs += i - good_pairs_count
            diff_count[diff] = good_pairs_count + 1

        return bad_pairs

print(Solution().countBadPairs([1,2,3,4,5]))