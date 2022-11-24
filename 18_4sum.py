class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        nums.sort()

        n = len(nums)

        for i in range(n):
            a = nums[i]

            if i > 0 and a == nums[i - 1]:
                continue

            for j in range(i + 1, n):
                b = nums[j]

                if j > i + 1 and b == nums[j - 1]:
                    continue

                l = n - 1

                for k in range(j + 1, n):
                    c = nums[k]

                    if k > j + 1 and c == nums[k - 1]:
                        continue

                    while k < l:
                        d = nums[l]

                        s = a + b + c + d

                        if s <= target:
                            break

                        l -= 1
                    else:
                        break

                    if s == target:
                        ans.append([a, b, c, d])

        return ans
