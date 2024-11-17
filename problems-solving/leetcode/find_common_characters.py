from typing import List
class Solution:
    def commonChars(self, words: List[str])-> List[str]:
        freq = {char: words[0].count(char) for char in words[0]}
        result = []
        for word in words:
            for key in freq.keys():
                count = word.count(key)
                if count < freq[key]:
                    freq[key] = count
        for key, value in freq.items():
            for i in range(value):
                result.append(key)
        return result