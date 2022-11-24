class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # return dfs(root, root)

        st = [(root, root)]

        while st:
            L, R = st.pop()

            if L and R:
                if L.val != R.val:
                    return False

                st += [(L.left, R.right), (L.right, R.left)]
            elif L or R:
                return False

        return True


def dfs(L: Optional[TreeNode], R: Optional[TreeNode]) -> bool:
    if L and R:
        return (
            L.val == R.val and dfs(L.left, R.right) and dfs(L.right, R.left)
        )

    return not (L or R)
