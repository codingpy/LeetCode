class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float("inf")

        nums.sort()

        n = len(nums)

        for i in range(n):
            a = nums[i]

            if i > 0 and a == nums[i - 1]:
                continue

            k = n - 1

            for j in range(i + 1, n):
                b = nums[j]

                if j > i + 1 and b == nums[j - 1]:
                    continue

                while j < k:
                    c = nums[k]

                    s = a + b + c

                    if abs(s - target) < abs(ans - target):
                        ans = s

                    if s <= target:
                        break

                    k -= 1
                else:
                    break

                if ans == target:
                    return target

        return ans
