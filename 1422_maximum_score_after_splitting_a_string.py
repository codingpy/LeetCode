class Solution:
    def maxScore(self, s: str) -> int:
        score = (s[0] == "0") + s[1:].count("1")

        ans = score

        for c in s[1:-1]:
            score += 1 if c == "0" else -1

            ans = max(ans, score)

        return ans
