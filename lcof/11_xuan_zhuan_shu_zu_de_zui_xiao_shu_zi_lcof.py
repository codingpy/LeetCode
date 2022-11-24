class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # return min(numbers)

        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            mid = (lo + hi) // 2

            if numbers[mid] > numbers[hi]:
                lo = mid + 1
            elif numbers[mid] < numbers[hi]:
                hi = mid
            else:
                hi -= 1

        return numbers[lo]
