class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return dfs(root, root)


def dfs(L: Optional[TreeNode], R: Optional[TreeNode]) -> bool:
    if L and R:
        return (
            L.val == R.val and dfs(L.left, R.right) and dfs(L.right, R.left)
        )

    return not (L or R)
