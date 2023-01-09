# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = answer = ListNode()
        while l1 or l2:
            if l1 and not l2:
                l2 = ListNode()
            if l2 and not l1:
                l1 = ListNode()
            
            if l1.val + l2.val > 9:
                answer.val = ((l1.val+l2.val) - 10)
                if not l1.next:
                    l1.next = ListNode()
                l1.next.val += 1
            else:
                answer.val = (l1.val+l2.val)
            l1=l1.next
            l2=l2.next
            if l1 or l2:
                answer.next = ListNode()
            answer = answer.next
        
        return temp
        
        