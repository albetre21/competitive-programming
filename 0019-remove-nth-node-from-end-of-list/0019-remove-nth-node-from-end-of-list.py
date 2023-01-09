# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newhead = head
        m = head
        l = head
        counter = 0
        counter_2 = 1
        while m:
            counter += 1
            m = m.next
 
        if counter == 1:
            return None
        
        if n == counter:
            newhead = newhead.next
        
        while l: 
            
            if counter_2  == counter - (n - 1) - 1:
                l.next = l.next.next
                break
            l = l.next
            counter_2 += 1
            
        return newhead   
       