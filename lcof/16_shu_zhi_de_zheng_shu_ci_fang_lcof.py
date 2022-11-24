class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x, n)


def pow(x: float, n: int) -> float:
    ans = 1

    if n < 0:
        x, n = 1 / x, -n

    while n:
        if n & 1:
            ans *= x

        x *= x

        n >>= 1

    return ans
