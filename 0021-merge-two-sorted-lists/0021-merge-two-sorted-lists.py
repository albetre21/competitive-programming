# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        res = answer = ListNode(None)
        ptr1, ptr2 = list1, list2
        while ptr1 or ptr2:
            if not ptr2:
                answer.val=ptr1.val
                ptr1=ptr1.next
                
            elif not ptr1:
                answer.val=ptr2.val
                ptr2=ptr2.next
                
            elif ptr1.val<ptr2.val:
                answer.val=ptr1.val
                ptr1=ptr1.next
            else:
                answer.val=ptr2.val
                ptr2=ptr2.next
            
            if ptr1 or ptr2:
                answer.next=ListNode()
                answer=answer.next
            
        return res