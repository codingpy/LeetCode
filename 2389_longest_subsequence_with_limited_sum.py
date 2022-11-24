from itertools import accumulate

from bisect import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sums = list(accumulate(sorted(nums)))

        return [bisect(sums, query) for query in queries]
