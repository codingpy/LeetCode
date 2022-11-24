class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        return josephus(n, m)


def josephus(n: int, k: int) -> int:
    s = 0

    for i in range(2, n + 1):
        s = (s + k) % i

    return s
