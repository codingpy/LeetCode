class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root:
            if root is p or root is q:
                return root

            L = self.lowestCommonAncestor(root.left, p, q)
            R = self.lowestCommonAncestor(root.right, p, q)

            if L and R:
                return root

            return L or R
