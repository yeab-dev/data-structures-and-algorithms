class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patterntoWordMap = {}
        wordToPatternMap = {}
        wordList = s.split()
        
        if len(wordList) != len(pattern):
            return False
        for i in range(len(pattern)):
            if not pattern[i] in patterntoWordMap:
                patterntoWordMap[pattern[i]] = wordList[i]
            else:
                if patterntoWordMap[pattern[i]] != wordList[i]:
                    return False
            if not wordList[i] in wordToPatternMap:
                wordToPatternMap[wordList[i]] = pattern[i]
            else:
                if not wordToPatternMap[wordList[i]] == pattern[i]:
                    return False
        return True