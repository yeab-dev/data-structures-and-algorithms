class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(sep=" ")
        for i in range(len(words)-1, 0, -1):
            if len(words[i]) > 0:
                return len(words[i])
        return(len(words[0]))
