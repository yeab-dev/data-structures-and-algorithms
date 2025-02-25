from typing import List
class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix_sum = [1] * len(logs)
        logs.sort(key=lambda x: x[0])
        for i in range(1, len(logs)):
            max_year = max(logs[i-1])
            j = i
            while j < len(logs) and max_year > min(logs[j]):
                prefix_sum[j] += 1
                j += 1
        max_population = max(prefix_sum)
        return logs[prefix_sum.index(max_population)][0]