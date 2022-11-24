class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return dfs(root) >= 0


def dfs(root: Optional[TreeNode]) -> int:
    if root:
        L = dfs(root.left)

        if L < 0:
            return L

        R = dfs(root.right)

        if R < 0:
            return R

        if abs(L - R) <= 1:
            return max(L, R) + 1

        return -1

    return 0
