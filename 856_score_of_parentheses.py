class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0

        left = 0

        for i, c in enumerate(s):
            if c == "(":
                left += 1
            else:
                left -= 1

                if s[i - 1] == "(":
                    ans += 1 << left

        return ans
