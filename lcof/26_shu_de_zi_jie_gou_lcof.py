class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if A and B:
            return (
                dfs(A, B)
                or self.isSubStructure(A.left, B)
                or self.isSubStructure(A.right, B)
            )

        return False


def dfs(A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
    if A and B:
        return A.val == B.val and dfs(A.left, B.left) and dfs(A.right, B.right)

    return not B
