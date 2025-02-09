from typing import List
class Solution:
    def findLHS(self, nums:List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        maxLength = 0
        currentLength = 0
        for i in freq.keys():
            if i+1 in freq:
                currentLength  = freq[i] + freq[i+1]
                if currentLength > maxLength:
                    maxLength = currentLength
        return maxLength