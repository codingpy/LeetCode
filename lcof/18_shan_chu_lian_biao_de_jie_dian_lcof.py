class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next

        head.next = self.deleteNode(head.next, val)

        return head
