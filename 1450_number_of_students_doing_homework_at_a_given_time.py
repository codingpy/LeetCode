from collections import defaultdict

from bisect import bisect


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        # return sum(a <= queryTime <= b for a, b in zip(startTime, endTime))

        diff = defaultdict(int)

        for a, b in zip(startTime, endTime):
            diff[a] += 1

            diff[b + 1] -= 1

        ans = []

        s = 0

        for k, v in sorted(diff.items()):
            if v:
                s += v

                ans.append((k, s))

        return ans[bisect(ans, queryTime, key=lambda x: x[0]) - 1][1]
