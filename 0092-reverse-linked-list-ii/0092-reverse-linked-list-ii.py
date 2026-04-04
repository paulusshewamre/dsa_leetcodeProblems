# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        prev = None
        cur = head
        i = left-1
        while cur and i > 0:
            prev = cur
            cur = cur.next
            i-=1
        
        last = prev
        newEnd = cur
        next = cur.next
        i=right-left+1

        while cur and i > 0:
            cur.next = prev
            prev = cur
            cur = next
            if next:
                next = next.next
            i-=1
        
        if last:
            last.next = prev
        else:
            head = prev
        
        newEnd.next = cur
        return head
        
