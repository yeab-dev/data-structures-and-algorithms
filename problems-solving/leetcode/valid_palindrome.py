from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
                if char.isupper():
                    chars.append(char.lower())
                else: chars.append(char)
        return "".join(chars) == "".join(chars[::-1])

print(Solution().isPalindrome("0P"))