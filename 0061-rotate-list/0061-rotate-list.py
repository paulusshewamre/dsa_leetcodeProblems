# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head
        if head == None:
            return head

        cnt = 0
        temp = head
        tail = None
        while temp:
            cnt+=1
            if temp.next == None:
                tail = temp
            temp = temp.next
        
        r = k % cnt
        if r == 0:
            return head

        temp = head
        for i in range(0, cnt - r-1):
            temp = temp.next
        
        newHead = temp.next
        temp.next = None
        tail.next = head

        return newHead
            
