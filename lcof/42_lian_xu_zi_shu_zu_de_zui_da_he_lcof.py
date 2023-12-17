class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ans = float('-inf')

        # s = 0

        # s_min = 0

        # for num in nums:
        #     s += num

        #     ans = max(ans, s - s_min)

        #     s_min = min(s_min, s)

        # return ans

        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)  # DP

        return max(nums)
