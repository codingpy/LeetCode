class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        a, b = 0, 13

        seen = set()

        for num in nums:
            if num != 0:
                a = max(a, num)
                b = min(b, num)

                if num in seen:
                    return False

                seen.add(num)

        return a - b < 5
