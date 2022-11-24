class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = set()

        dic = {}

        def dfs(root: Optional[TreeNode]) -> int:
            if root:
                key = root.val, dfs(root.left), dfs(root.right)

                if key in dic:
                    root = dic[key]

                    ans.add(root)
                else:
                    dic[key] = root

            return id(root)

        dfs(root)

        return list(ans)
