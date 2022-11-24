class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo = bisect_left(nums, target)

        hi = bisect(nums, target)

        return [lo, hi - 1] if lo < hi else [-1, -1]


def bisect_left(a, x):
    lo = 0

    hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid

    return lo


def bisect(a, x):
    lo = 0

    hi = len(a)

    while lo < hi:
        mid = (lo + hi) // 2

        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1

    return lo
