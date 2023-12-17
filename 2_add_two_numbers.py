class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()

        cur = dummy

        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            s = val1 + val2 + carry

            cur.next = ListNode(val=s % 10)

            cur = cur.next

            carry = s // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry:
            cur.next = ListNode(val=carry)

        return dummy.next
