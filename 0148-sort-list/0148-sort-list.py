# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        dup=head
        while dup:
            arr.append(dup.val)
            dup=dup.next
        arr.sort()
        h=head
        for i in arr:
            h.val=i
            h=h.next
        return head