class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        sub_lengths = []
        win = s[start: end]
        for char in s:
            while char in win and start < end:
                sub_lengths.append(len(win))
                start += 1
                win = s[start: end]
            else: 
                end += 1 
            win = s[start: end]
        sub_lengths.append(len(win))
        return max(sub_lengths)