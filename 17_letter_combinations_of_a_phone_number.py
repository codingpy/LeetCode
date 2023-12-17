class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        ans = [""]

        for digit in digits:
            letters = phone[int(digit)]

            ans = [combination + letter for combination in ans for letter in letters]

        return ans
