import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        cx = 0
        cy = 0

        q_max = 0

        for x in range(51):
            for y in range(51):
                q = 0

                for xi, yi, qi in towers:
                    d = math.dist((xi, yi), (x, y))

                    if d <= radius:
                        q += qi // (1 + d)

                if q_max < q:
                    q_max = q

                    cx = x
                    cy = y

        return [cx, cy]
