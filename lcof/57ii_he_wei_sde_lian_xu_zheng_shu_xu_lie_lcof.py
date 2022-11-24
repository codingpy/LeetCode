class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ans = []

        n = 1

        while target > 0:
            q, r = divmod(target, n)

            if r == 0:
                ans.append(list(range(q, q + n)))

            target -= n

            n += 1

        return ans[:0:-1]
