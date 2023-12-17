class Solution:
    def reverseWords(self, s: str) -> str:
        # return ' '.join(reversed(s.split()))

        s = list(s)

        # Reduce multiple spaces between two words to a single space

        n = len(s)

        i = 0

        for j in range(n):
            if s[j] != " ":
                if i > 0:
                    if s[j - 1] == " ":
                        s[i] = " "

                        i += 1

                s[i] = s[j]

                i += 1

        s = s[:i]

        # Reverse the order of the words

        def reverse(i: int, j: int) -> None:
            while i < j:
                s[i], s[j] = s[j], s[i]

                i += 1
                j -= 1

        n = len(s)

        reverse(0, n - 1)

        i = 0

        for j in range(n):
            if s[j] != " ":
                if j + 1 == n or s[j + 1] == " ":
                    reverse(i, j)
            else:
                i = j + 1

        return "".join(s)
