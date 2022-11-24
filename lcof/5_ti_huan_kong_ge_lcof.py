class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(' ', '%20')

        i = len(s) - 1

        s = list(s + '  ' * s.count(' '))

        j = len(s) - 1

        while i < j:
            c = s[i]

            if c == ' ':
                s[j - 2] = '%'
                s[j - 1] = '2'
                s[j] = '0'

                j -= 3
            else:
                s[j] = c

                j -= 1

            i -= 1

        return ''.join(s)
