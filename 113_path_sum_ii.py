class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root:
            if root.left or root.right:
                return [[root.val] + path for path in (
                    self.pathSum(root.left, targetSum - root.val)
                    + self.pathSum(root.right, targetSum - root.val)
                )]

            if root.val == targetSum:
                return [[root.val]]

        return []
