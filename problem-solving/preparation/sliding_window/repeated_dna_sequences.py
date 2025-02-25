from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result_set = set()
        for i in range(len(s) - 9):
            win = s[i:i+10]
            if win in seen:
                result_set.add(win)
            seen.add(win)
        return list(result_set)