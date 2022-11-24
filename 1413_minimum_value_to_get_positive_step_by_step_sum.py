from itertools import accumulate


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        return 1 - min(min(accumulate(nums)), 0)
