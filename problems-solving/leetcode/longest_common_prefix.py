from typing import List


class Solution():
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = strs[0][0]
        for str in strs:
            if str.startswith(l):
                continue