class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        s = list(s)

        def backtrack(i: int) -> None:
            if i == len(s):
                ans.append("".join(s))

                return

            backtrack(i + 1)

            if s[i].isalpha():
                s[i] = s[i].swapcase()

                backtrack(i + 1)

        backtrack(0)

        return ans
