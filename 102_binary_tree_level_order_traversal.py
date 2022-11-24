from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        if root:
            q = deque([root])

            while q:
                level = []

                for _ in range(len(q)):
                    root = q.popleft()

                    level.append(root.val)

                    if root.left:
                        q.append(root.left)

                    if root.right:
                        q.append(root.right)

                ans.append(level)

        return ans
