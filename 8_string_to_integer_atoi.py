INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

UINT_MAX = 2 ** 32 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        return atoi(s)


def atoi(s: str) -> int:
    i = 0

    # skip white space

    while i < len(s) and s[i] == ' ':
        i += 1

    # check for a sign

    negative = False

    if i < len(s):
        if s[i] == '-':
            negative = True

            i += 1
        elif s[i] == '+':
            i += 1

    # avoid runtime division

    cutoff, cutlim = divmod(UINT_MAX, 10)

    overflow = False

    j = 0

    while i < len(s) and '0' <= s[i] <= '9':
        c = ord(s[i]) - ord('0')

        # check for overflow

        if j > cutoff or (j == cutoff and c > cutlim):
            overflow = True

            break

        j = j * 10 + c

        i += 1
    else:
        if j > (-(INT_MIN + 1) + 1 if negative else INT_MAX):
            overflow = True

    if overflow:
        return INT_MIN if negative else INT_MAX

    # return the result of the appropriate sign

    return -j if negative else j
