class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if stack[-len(part):] == list(part):
                for j in range(len(part)):
                    stack.pop()
        return "".join(stack)
