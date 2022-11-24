class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        i, j = 0, len(height) - 1

        while i < j:
            h1 = height[i]
            h2 = height[j]

            ans = max(ans, min(h1, h2) * (j - i))

            if h1 < h2:
                i += 1
            else:
                j -= 1

        return ans
