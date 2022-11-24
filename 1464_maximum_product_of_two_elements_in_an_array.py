class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # a, b = heapq.nlargest(2, nums)

        a, b = 0, 0

        for num in nums:
            if a < num:
                a, b = num, a
            elif b < num:
                b = num

        return (a - 1) * (b - 1)
