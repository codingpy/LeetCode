from itertools import accumulate

from collections import deque


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = n + 1

        sums = list(accumulate(nums, initial=0))

        q = deque()

        for i, val in enumerate(sums):
            while q and val - sums[q[0]] >= k:
                ans = min(ans, i - q.popleft())

            while q and sums[q[-1]] >= val:
                q.pop()

            q.append(i)

        return ans if ans <= n else -1
