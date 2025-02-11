from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        i = 0
        points.sort(key=lambda x: x[1])
        while i < len(points):
            arrow = points[i][1]
            while i < len(points) and arrow >= points[i][0]:
                i += 1
            count += 1
        return count