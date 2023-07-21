#https://leetcode.com/problems/fibonacci-number/description/

class Solution:

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-1)

    def fib2(self, n: int) -> int:
        cache = {}

        def helper(n):
            if n <= 1:
                return n
            if n in cache:
                return cache[n]
            result = helper(n-1) + helper(n-2)

            cache[n] = result

            return cache[n]
        return helper(n)

"""
Time Complexity -> O(n)
Space Complexity -> O(1)
"""