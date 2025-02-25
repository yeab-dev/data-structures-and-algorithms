class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            elif stack[-1] == char:
                stack.pop()
        return "".join(stack)