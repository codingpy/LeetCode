class Solution:
    def printNumbers(self, n: int) -> List[int]:
        # return list(range(1, 10 ** n))

        ans = [""]

        for _ in range(n):
            ans = [
                combination + str(digit) for combination in ans for digit in range(10)
            ]

        return list(map(int, ans[1:]))
