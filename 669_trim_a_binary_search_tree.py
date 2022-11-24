class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if root:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)

            if low <= root.val <= high:
                return root

            return root.left or root.right
