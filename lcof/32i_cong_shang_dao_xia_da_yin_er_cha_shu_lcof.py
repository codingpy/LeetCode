from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []

        q = deque([root])

        while q:
            root = q.popleft()

            if root:
                ans.append(root.val)

                q += [root.left, root.right]

        return ans
