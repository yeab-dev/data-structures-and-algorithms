class Solution:
    def repeatedCharacter(self, s: str) -> str:
        stack = []
        for char in s:
            if char in stack:
                return char
            stack.append(char)