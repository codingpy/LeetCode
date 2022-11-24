INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1


class Solution:
    def reverse(self, x: int) -> int:
        ans = 0

        while x:
            if ans < INT_MIN // 10 + 1 or ans > INT_MAX // 10:
                return 0

            digit = x % 10

            if x < 0 and digit > 0:
                digit -= 10

            ans = ans * 10 + digit

            x = (x - digit) // 10

        return ans
