class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # return list(Counter(t) - Counter(s))[0]

        ans = 0

        for c in s:
            ans ^= ord(c)

        for c in t:
            ans ^= ord(c)

        return chr(ans)
