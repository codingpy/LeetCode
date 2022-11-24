class Solution:
    def isUnique(self, astr: str) -> bool:
        bits = 0

        for c in astr:
            bit = 1 << ord(c) - ord('a')

            if bits & bit:
                return False

            bits |= bit

        return True
