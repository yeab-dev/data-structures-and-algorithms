from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        i = 0
        while i < len(nums):
            heapq.heappush(heap, nums[i])
            if len(heap) == k+1:
                heapq.heappop(heap)
            i += 1
        return heap[0]