from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        G = defaultdict(list)

        for a, b in dislikes:
            G[a].append(b)
            G[b].append(a)

        return is_bipartite(G)


def is_bipartite(G):
    try:
        color(G)

        return True
    except ValueError:
        return False


def color(G):
    dic = {}

    def dfs(u, c):
        dic[u] = c

        for v in G[u]:
            if v not in dic:
                dfs(v, 1 - c)
            elif dic[v] == c:
                raise ValueError("Graph is not bipartite.")

    for u in G:
        if u not in dic:
            dfs(u, 1)

    return dic
