class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # return heapq.nsmallest(k, arr)

        qselect(arr, k, 0, len(arr) - 1)

        return arr[:k]


# Places the kth smallest element in the kth position
# Because arrays start at 0, this will be index k-1

def qselect(
        a: List[int], k: int, left: int, right: int, cutoff: int = 3
) -> None:
    if left + cutoff <= right:
        pivot = median3(a, left, right)

        i = left
        j = right - 1

        while True:
            i += 1
            j -= 1

            while a[i] < pivot:
                i += 1

            while a[j] > pivot:
                j -= 1

            if i < j:
                a[i], a[j] = a[j], a[i]
            else:
                break

        a[i], a[right - 1] = a[right - 1], a[i]  # Restore pivot

        if k <= i:
            qselect(a, k, left, i - 1)
        elif k > i + 1:
            qselect(a, k, i + 1, right)
    else:
        # Do an insertion sort on the subarray

        x = a[left : right + 1]

        insertion_sort(x)

        a[left : right + 1] = x


# Return median of Left, Center, and Right
# Order these and hide the pivot

def median3(a: List[int], left: int, right: int) -> int:
    center = (left + right) // 2

    if a[left] > a[center]:
        a[left], a[center] = a[center], a[left]

    if a[left] > a[right]:
        a[left], a[right] = a[right], a[left]

    if a[center] > a[right]:
        a[center], a[right] = a[right], a[center]

    # Invariant: A[ Left ] <= A[ Center ] <= A[ Right ]

    a[center], a[right - 1] = a[right - 1], a[center]  # Hide pivot

    return a[right - 1]  # Return pivot


def insertion_sort(a: List[int]) -> None:
    n = len(a)

    for j in range(1, n):
        tmp = a[j]

        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]

            j -= 1

        a[j] = tmp
