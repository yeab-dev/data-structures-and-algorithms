from typing import List
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for char in s:
            if char.isnumeric():
                if stack != []:
                    stack.pop()
                continue
            
            stack.append(char)
        return "".join(stack)
