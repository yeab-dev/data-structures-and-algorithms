from typing import List
class Solution:
    def queryResults(self, limit:int, queries: List[List[int]]) -> List[int]:
        result = []
        colorMap = {}
        ballMap = {}

        for query in queries:
            ball = query[0]
            color = query[1]
            if ball in ballMap:
                prevColor = ballMap[ball]
                colorMap[prevColor] -= 1
                if colorMap[prevColor] == 0:
                    del colorMap[prevColor]
            ballMap[ball] = color
            if not color in colorMap:
                colorMap[color] = 1
            else:
                colorMap[color] += 1
            result.append(len(colorMap))
        return result