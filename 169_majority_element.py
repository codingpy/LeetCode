class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return mjrty(nums)


def mjrty(a: List[int]) -> Optional[int]:
    cand = 0

    # pairing

    k = 0

    for x in a:
        if k == 0:
            cand = x

        if cand == x:
            k += 1
        else:
            k -= 1

    if k > 0:
        n = len(a)

        if k > n // 2:
            return cand

        # counting

        k = 0

        for x in a:
            if cand == x:
                k += 1

                if k > n // 2:
                    return cand
