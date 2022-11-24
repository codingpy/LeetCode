class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, num in enumerate(nums):
            residue = target - num

            if residue in dic:
                return [dic[residue], i]

            dic[num] = i

        return []
