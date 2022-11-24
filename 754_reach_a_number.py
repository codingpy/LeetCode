import math


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)

        n = math.ceil(solve(1, 1, -2 * target))

        if (n * (n + 1) / 2 - target) % 2 == 0:
            return n

        if n % 2 == 0:
            return n + 1

        return n + 2


def solve(a: float, b: float, c: float) -> float:  # quadratic
    return (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
