class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # return [[math.comb(n, k) for k in range(n + 1)] for n in range(numRows)]

        ans = [[1]]

        for _ in range(numRows - 1):
            ans.append([
                a + b for a, b in zip([0] + ans[-1], ans[-1] + [0])
            ])

        return ans
