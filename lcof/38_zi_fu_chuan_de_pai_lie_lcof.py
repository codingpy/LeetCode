class Solution:
    def permutation(self, s: str) -> List[str]:
        # return list({''.join(x) for x in itertools.permutations(s)})

        ans = []

        s = sorted(s)

        while True:
            ans.append("".join(s))

            if not next_permutation(s):
                return ans


def next_permutation(perm: List[int]) -> bool:
    n = len(perm)

    i = n - 2

    while i >= 0 and perm[i] >= perm[i + 1]:
        i -= 1

    ans = i >= 0

    if ans:
        j = n - 1

        while perm[i] >= perm[j]:
            j -= 1

        perm[i], perm[j] = perm[j], perm[i]

    l = i + 1
    r = n - 1

    while l < r:
        perm[l], perm[r] = perm[r], perm[l]

        l += 1
        r -= 1

    return ans
