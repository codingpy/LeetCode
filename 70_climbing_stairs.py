class Solution:
    def climbStairs(self, n: int) -> int:
        return fib(n + 1)


def fib(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
