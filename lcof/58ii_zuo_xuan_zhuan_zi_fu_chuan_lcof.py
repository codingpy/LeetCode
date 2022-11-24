class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # return s[n:] + s[:n]

        s = list(s)

        def reverse(i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]

                i += 1
                j -= 1

        m = len(s)

        reverse(0, n - 1)
        reverse(n, m - 1)
        reverse(0, m - 1)

        return ''.join(s)
