class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        next_permutation(nums)


def next_permutation(perm: List[int]) -> bool:
    n = len(perm)

    i = n - 2

    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    ans = i >= 0

    if ans:
        j = n - 1

        while perm[i] >= perm[j]:
            j -= 1

        perm[i], perm[j] = perm[j], perm[i]

    l = i + 1
    r = n - 1

    while l < r:
        perm[l], perm[r] = perm[r], perm[l]

        l += 1
        r -= 1

    return ans
