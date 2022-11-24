class Solution:
    def numWays(self, n: int) -> int:
        return fib(n + 1) % 1_000_000_007


def fib(n: int) -> int:
    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a
