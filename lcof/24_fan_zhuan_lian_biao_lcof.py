class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev
