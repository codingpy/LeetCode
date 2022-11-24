class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # h = [1]

        # factors = [2, 3, 5]

        # seen = set()

        # for _ in range(n):
        #     ans = heapq.heappop(h)

        #     for factor in factors:
        #         num = ans * factor

        #         if num not in seen:
        #             heapq.heappush(h, num)

        #             seen.add(num)

        # return ans

        dp = [1]

        i = 0
        j = 0
        k = 0

        for _ in range(n - 1):
            a = dp[i] * 2
            b = dp[j] * 3
            c = dp[k] * 5

            num = min(a, b, c)

            i += num == a
            j += num == b
            k += num == c

            dp.append(num)

        return dp[-1]
