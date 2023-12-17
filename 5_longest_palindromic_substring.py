class Solution:
    def longestPalindrome(self, s: str) -> str:
        i, j = 0, 1

        def expand(i: int, j: int) -> int:
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1

            return j - i - 1

        for center in range(len(s)):
            maxlen = max(expand(center, center), expand(center - 1, center))

            if j - i < maxlen:
                i, j = center - maxlen // 2, center + (maxlen + 1) // 2

        return s[i:j]
