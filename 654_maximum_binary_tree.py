class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        st = []

        for val in nums:
            root = TreeNode(val)

            while st and st[-1].val < val:
                root.left = st.pop()

            if st:
                st[-1].right = root

            st.append(root)

        return st[0]
