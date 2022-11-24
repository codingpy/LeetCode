class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        lo = 4 * k

        hi = 5 * k + 1

        while lo < hi:
            mid = (lo + hi) // 2

            zeroes = nu(mid, 5)

            if zeroes < k:
                lo = mid + 1
            elif zeroes > k:
                hi = mid
            else:
                return 5

        return 0


def nu(n: int, p: int) -> int:
    ans = 0

    while n:
        n //= p

        ans += n

    return ans
