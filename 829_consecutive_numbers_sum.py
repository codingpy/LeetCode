class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        ans = 0

        i = 1

        while n > 0:
            if n % i == 0:
                ans += 1

            n -= i

            i += 1

        return ans
