class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        # n = len(nums) + 2

        # bit = 0

        # for num in nums:
        #     bit ^= num

        # for num in range(1, n + 1):
        #     bit ^= num

        # bit &= -bit

        # a, b = 0, 0

        # for num in nums:
        #     if num & bit:
        #         a ^= num
        #     else:
        #         b ^= num

        # for num in range(1, n + 1):
        #     if num & bit:
        #         a ^= num
        #     else:
        #         b ^= num

        # return [a, b]

        n = len(nums) + 2

        s = (n + 1) * n // 2 - sum(nums)

        m = s // 2

        a = (m + 1) * m // 2 - sum(num for num in nums if num <= m)

        return [a, s - a]
