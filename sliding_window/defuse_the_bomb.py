from typing import List
class Solution:
    def decrcypt(self, code: List[int], k: int):
        length = len(code)
        res = [0] * length
        range_sum = 0
        for i in range(length):
            if k > 0:
                for j in range(i + 1, i + 1 + k):
                   res[i] += code[j % length] 
            
            elif k < 0:
                for j in range(i-1, i - 1 - abs(k), -1):
                    res[i] += code[j % length]
        
        return res