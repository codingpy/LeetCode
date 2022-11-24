class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0

        j = 0

        for i, num in enumerate(arr):
            j = max(j, num)

            if i == j:
                ans += 1

        return ans
