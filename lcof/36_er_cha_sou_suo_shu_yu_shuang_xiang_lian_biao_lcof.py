class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if root:
            li = inorder(root)

            for prev, cur in zip(li[-1:] + li, li):
                prev.right = cur

                cur.left = prev

            return li[0]


def inorder(root: "Optional[Node]") -> "List[Node]":
    return inorder(root.left) + [root] + inorder(root.right) if root else []
