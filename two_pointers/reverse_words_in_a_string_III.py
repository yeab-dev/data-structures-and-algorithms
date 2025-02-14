class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)

        def reverse(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        
        start = 0

        for i in range(len(chars) + 1):
            if i == len(chars) or chars[i] == " ":
                reverse(start, i - 1)
                start = i + 1

        return "".join(chars)