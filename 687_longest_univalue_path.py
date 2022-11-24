class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            L = dfs(root.left) + 1

            if root.left is None or root.left.val != root.val:
                L = 0

            R = dfs(root.right) + 1

            if root.right is None or root.right.val != root.val:
                R = 0

            nonlocal ans

            ans = max(ans, L + R)

            return max(L, R)

        dfs(root)

        return ans
