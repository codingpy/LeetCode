class Solution:
    def trailingZeroes(self, n: int) -> int:
        return nu(n, 5)


def nu(n: int, p: int) -> int:  # Legendre
    ans = 0

    while n:
        n //= p

        ans += n

    return ans
