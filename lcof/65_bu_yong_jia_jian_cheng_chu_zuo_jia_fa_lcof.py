UINT_MAX = 0xFFFFFFFF  # 2 ** 32 - 1


class Solution:
    def add(self, a: int, b: int) -> int:
        while b:
            a, b = a ^ b, (a & b) << 1 & UINT_MAX

        # c_int

        a &= UINT_MAX

        if a & 0x80000000:
            a = ~(a ^ UINT_MAX)

        return a
