# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        
        while True:
            if b.next == None:
                return a
            
            if b.next.next == None:
                return a.next
             
            a = a.next
            b = b.next.next
        