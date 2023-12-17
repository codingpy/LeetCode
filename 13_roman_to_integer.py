class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0

        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        for i, c in enumerate(s):
            num = roman[c]

            if i + 1 < len(s) and num < roman[s[i + 1]]:
                ans -= num
            else:
                ans += num

        return ans
