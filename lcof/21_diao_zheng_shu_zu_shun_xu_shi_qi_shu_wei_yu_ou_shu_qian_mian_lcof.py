class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        # return (
        #     [num for num in nums if num % 2 == 1]
        #     + [num for num in nums if num % 2 == 0]
        # )

        i = 0

        for j in range(len(nums)):
            if nums[j] % 2 == 1:
                nums[i], nums[j] = nums[j], nums[i]

                i += 1

        return nums
