from functools import cmp_to_key


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        return ''.join(sorted(
            map(str, nums), key=cmp_to_key(lambda a, b: int(a + b) - int(b + a))
        ))
