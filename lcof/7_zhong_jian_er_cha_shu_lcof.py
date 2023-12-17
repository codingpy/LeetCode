class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {val: i for i, val in enumerate(inorder)}

        def dfs(
            preorder_root: int, inorder_left: int, inorder_right: int
        ) -> Optional[TreeNode]:
            if inorder_left < inorder_right:
                val = preorder[preorder_root]

                root = TreeNode(val)

                i = dic[val]

                root.left = dfs(preorder_root + 1, inorder_left, i)
                root.right = dfs(
                    preorder_root + 1 + (i - inorder_left), i + 1, inorder_right
                )

                return root

        return dfs(0, 0, len(inorder))
