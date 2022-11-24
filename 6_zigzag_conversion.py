class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        ans = []

        t = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, len(s) - i, t):
                ans.append(s[i + j])

                if 0 < i < numRows - 1 and j + t - i < len(s):
                    ans.append(s[j + t - i])

        return ''.join(ans)
