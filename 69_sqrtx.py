class Solution:
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))


def sqrt(x: float, eps: float = 1e-7) -> float:  # newton
    if not x:
        return 0

    x0 = x

    while True:
        xi = 0.5 * (x0 + x / x0)

        if x0 - xi < eps:
            return xi

        x0 = xi
