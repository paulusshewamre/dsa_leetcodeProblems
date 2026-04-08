class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        d1h = dummy1
        d2h = dummy2

        cur = head

        while cur:
            if cur.val < x:
                d1h.next = cur
                d1h = cur
            else:
                d2h.next = cur
                d2h = cur
            cur = cur.next

        d2h.next = None

        d1h.next = dummy2.next

        return dummy1.next