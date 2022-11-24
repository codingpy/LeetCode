class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        st1 = [root]

        st2 = []

        while st1 or st2:
            level = []

            while st1:
                root = st1.pop()

                if root:
                    level.append(root.val)

                    st2 += [root.left, root.right]

            if level:
                ans.append(level)

            level = []

            while st2:
                root = st2.pop()

                if root:
                    level.append(root.val)

                    st1 += [root.right, root.left]

            if level:
                ans.append(level)

        return ans
