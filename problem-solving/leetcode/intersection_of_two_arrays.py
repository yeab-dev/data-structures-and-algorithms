from typing import List
class Solution:
    def intersection(self,nums1: List[int], nums2: List[int]) -> List[int]:
        intersection: List[int] = []
        for number in nums1:
            if number in nums2 and not(number in intersection):
                intersection.append(number)
        
        return intersection
                
