class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return josephus(n, k) + 1


def josephus(n: int, k: int) -> int:
    s = 0

    for i in range(2, n + 1):
        s = (s + k) % i

    return s
