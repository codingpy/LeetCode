class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

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

                    if s <= 0:
                        break

                    k -= 1
                else:
                    break

                if s == 0:
                    ans.append([a, b, c])

        return ans
