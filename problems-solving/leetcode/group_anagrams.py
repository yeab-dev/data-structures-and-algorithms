from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                freq[index] += 1
            signature = tuple(freq)
            if signature not in word_map:
                word_map[signature] = [word]
            else:
                word_map[signature].append(word)
        
        return list(word_map.values())