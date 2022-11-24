from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        for k, v in Counter(s).items():
            if v == 1:
                return k

        return ' '
