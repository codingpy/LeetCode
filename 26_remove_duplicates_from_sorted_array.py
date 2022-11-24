class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if nums[i] != num:
                i += 1

                nums[i] = num

        return i + 1
