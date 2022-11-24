class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')

        ans = 0

        while n:
            ans += 1

            n &= n - 1

        return ans


def swar(n: int) -> int:
    n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
    n = (n * 0x01010101) >> 24

    return n & 0xff
