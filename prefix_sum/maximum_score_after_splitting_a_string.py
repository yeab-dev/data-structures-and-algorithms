class Solution:
    def maxScore(self, s: str):
        result = 0
        
        total_ones = s.count("1")
        left_zeroes = 0
        right_ones = total_ones
        for i in range(len(s)-1):
            if s[i]== '0':
                left_zeroes += 1
            elif s[i] == '1':
                right_ones -= 1
            result = max(result, left_zeroes+right_ones)
        return result

print(Solution().maxScore("011101"))