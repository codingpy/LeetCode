class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0

        for i, num in enumerate(nums):
            if i == 0 or num <= nums[i - 1]:
                s = 0

            s += num

            ans = max(ans, s)

        return ans
