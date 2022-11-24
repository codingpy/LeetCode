class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 1

        for num in nums:
            if not max_jump:
                return False

            max_jump = max(max_jump - 1, num)

        return True
