class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0

        max_pos = 0

        next_max_pos = 0

        for i in range(len(nums) - 1):
            next_max_pos = max(next_max_pos, i + nums[i])

            if i == max_pos:
                ans += 1

                max_pos = next_max_pos

        return ans
