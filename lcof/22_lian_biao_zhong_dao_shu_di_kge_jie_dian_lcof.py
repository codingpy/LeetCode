class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        tail = head

        for _ in range(k):
            tail = tail.next

        while tail:
            head = head.next
            tail = tail.next

        return head
