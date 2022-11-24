class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        bit = 0

        for num in nums:
            bit ^= num

        bit &= -bit

        a, b = 0, 0

        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
