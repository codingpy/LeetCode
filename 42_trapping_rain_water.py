class Solution:
    def trap(self, height: List[int]) -> int:
        # ans = 0

        # st = []

        # for j in range(len(height)):
        #     while st and height[st[-1]] < height[j]:
        #         i = st.pop()

        #         if st:
        #             ans += (
        #                 (j - st[-1] - 1)
        #                 * (min(height[st[-1]], height[j]) - height[i])
        #             )

        #     st.append(j)

        # return ans

        ans = 0

        h1 = 0

        h2 = 0

        n = len(height)

        for i in range(n):
            h1 = max(h1, height[i])

            h2 = max(h2, height[-(i + 1)])

            ans += h1 + h2 - height[i]

        return ans - h1 * n
