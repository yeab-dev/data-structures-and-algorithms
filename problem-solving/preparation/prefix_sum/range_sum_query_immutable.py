from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSum = []
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        self.prefixSum = nums

    def sumRange(self, left: int, right: int) -> int:
        prefixSum = self.prefixSum
        if(left ==0): 
            return prefixSum[right]
        
        return prefixSum[right] - prefixSum[left-1]