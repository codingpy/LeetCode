class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = get_height(root)

        m = height + 1

        n = 2 ** m - 1

        res = [[''] * n for _ in range(m)]

        def dfs(root: Optional[TreeNode], r: int, c: int) -> None:  # noqa
            if root:
                res[r][c] = str(root.val)

                dfs(root.left, r + 1, c - 2 ** (height - r - 1))
                dfs(root.right, r + 1, c + 2 ** (height - r - 1))

        dfs(root, 0, (n - 1) // 2)

        return res


def get_height(root: Optional[TreeNode]) -> int:
    return max(get_height(root.left), get_height(root.right)) + 1 if root else -1
