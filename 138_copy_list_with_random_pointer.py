class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # return copy.deepcopy(head)

        if head:
            cur = head

            while cur:
                cur.next = Node(cur.val, next=cur.next)

                cur = cur.next.next

            cur = head

            while cur:
                if cur.random:
                    cur.next.random = cur.random.next

                cur = cur.next.next

            cur = head.next

            while cur.next:
                cur.next = cur.next.next

                cur = cur.next

            return head.next
