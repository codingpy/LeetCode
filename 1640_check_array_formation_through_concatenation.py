class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {x[0]: x for x in pieces}

        return [y for x in arr for y in dic.get(x, [])] == arr
