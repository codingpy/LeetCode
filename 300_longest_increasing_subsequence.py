from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = []

        # for j in range(len(nums)):
        #     dp.append(1)

        #     for i in range(j):
        #         if nums[i] < nums[j]:
        #             dp[j] = max(dp[j], dp[i] + 1)

        # return max(dp)

        tails = []

        for num in nums:
            if tails and num <= tails[-1]:
                tails[bisect_left(tails, num)] = num
            else:
                tails.append(num)

        return len(tails)
