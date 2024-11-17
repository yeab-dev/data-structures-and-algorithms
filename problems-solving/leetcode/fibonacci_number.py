class Solution:
    def fib(self, num: int) -> int:
        if num == 0: return 0
        elif num == 1: return 1
        else: return self.fib(num-2) + self.fib(num-1)