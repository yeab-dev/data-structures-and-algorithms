def guess(number):
    pick = 1
    if number > pick:
        return -1
    elif number < pick:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 0
        high = n
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            g = guess(mid)
            if g == -1:
                high = mid - 1
            elif g == 1:
                low = mid + 1
            elif g == 0:
                return mid

print(Solution().guessNumber(1))