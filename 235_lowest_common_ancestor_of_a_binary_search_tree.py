class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p

        while True:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                return root
