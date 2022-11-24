class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        num = 1

        while num <= n:
            q, r = divmod(n, num * 10)

            ans += q * num + min(max(r - num + 1, 0), num)

            num *= 10

        return ans
