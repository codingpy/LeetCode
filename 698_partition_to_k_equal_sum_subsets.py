class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        q, r = divmod(sum(nums), k)

        if r != 0:
            return False

        nums.sort(reverse=True)

        if nums[0] > q:
            return False

        sums = [0] * k

        def backtrack(i: int) -> bool:
            if i == len(nums):
                return True

            for j in range(k):
                sums[j] += nums[i]

                if sums[j] <= q and backtrack(i + 1):
                    return True

                sums[j] -= nums[i]

                if sums[j] == 0:
                    break

            return False

        return backtrack(0)
