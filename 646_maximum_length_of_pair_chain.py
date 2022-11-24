class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans = 0

        b = float('-inf')

        for c, d in sorted(pairs, key=lambda x: x[1]):
            if b < c:
                ans += 1

                b = d

        return ans
