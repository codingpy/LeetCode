class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect(nums, target) - bisect_left(nums, target)


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
