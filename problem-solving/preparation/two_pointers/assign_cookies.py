from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        level_of_greeds = sorted(g)
        size_of_cookies = sorted(s)
        count = 0

        i, j = 0,0
        while i < len(level_of_greeds) and j < len(size_of_cookies):
            if level_of_greeds[i] <= size_of_cookies[j]:
                count += 1
                i += 1
                j += 1
            else: 
                j += 1
        return count
