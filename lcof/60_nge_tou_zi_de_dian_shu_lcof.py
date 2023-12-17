class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        dp = [1] + 5 * n * [0]

        for i in range(n):
            for j in range(5 * i, -1, -1):
                for k in range(1, 6):
                    dp[j + k] += dp[j]

        return [x / 6**n for x in dp]
