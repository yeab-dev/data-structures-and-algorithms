class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            win = s[i]
            j = i+1
            while (win.count("0") <= k or win.count("1") <= k) and j <= len(s):
                count += 1
                j += 1
                win = s[i: j]
        return count