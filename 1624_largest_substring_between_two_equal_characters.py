class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        dic = {}

        for i, c in enumerate(s):
            ans = max(ans, i - dic.setdefault(c, i + 1))

        return ans
