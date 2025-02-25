class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        x = list(s)
        x.append(x.pop(0))
        for i in range(len(s)):
            x.append(x.pop(0))
            if "".join(x) == goal:
                return True
        return False