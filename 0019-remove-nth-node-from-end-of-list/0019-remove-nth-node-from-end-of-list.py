# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        if cnt == n:
            return head.next

        temp = head
        for i in range(cnt-n-1):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return head
