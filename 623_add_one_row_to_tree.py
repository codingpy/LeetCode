class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if root:
            if depth == 1:
                root = TreeNode(val, left=root)
            elif depth == 2:
                root.left = TreeNode(val, left=root.left)
                root.right = TreeNode(val, right=root.right)
            else:
                root.left = self.addOneRow(root.left, val, depth - 1)
                root.right = self.addOneRow(root.right, val, depth - 1)

            return root
