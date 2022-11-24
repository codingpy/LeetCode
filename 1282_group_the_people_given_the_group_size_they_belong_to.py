from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []

        dic = defaultdict(list)

        for i, size in enumerate(groupSizes):
            group = dic[size]

            group.append(i)

            if len(group) == size:
                ans.append(dic.pop(size))

        return ans
