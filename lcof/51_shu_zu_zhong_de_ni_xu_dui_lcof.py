class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ans = 0

        def msort(a: List[int]) -> None:
            if len(a) > 1:
                mid = len(a) // 2

                L = a[:mid]
                R = a[mid:]

                msort(L)
                msort(R)

                i = 0
                j = 0
                k = 0

                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        a[k] = L[i]

                        i += 1
                    else:
                        a[k] = R[j]

                        j += 1

                        nonlocal ans

                        ans += len(L) - i

                    k += 1

                if i < len(L):
                    a[k:] = L[i:]

                if j < len(R):
                    a[k:] = R[j:]

        msort(nums)

        return ans
