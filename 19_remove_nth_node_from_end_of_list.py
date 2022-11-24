class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        head, tail = dummy, head

        for _ in range(n):
            tail = tail.next

        while tail:
            head = head.next
            tail = tail.next

        head.next = head.next.next

        return dummy.next
