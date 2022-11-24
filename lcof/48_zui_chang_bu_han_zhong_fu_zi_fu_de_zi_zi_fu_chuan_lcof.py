class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        dic = {}

        i = -1

        for j, c in enumerate(s):
            if c in dic:
                i = max(i, dic[c])

            ans = max(ans, j - i)

            dic[c] = j

        return ans
