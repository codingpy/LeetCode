from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)

        for i in sandwiches:
            if cnt[i] == 0:
                break

            cnt[i] -= 1

        return cnt[0] + cnt[1]
