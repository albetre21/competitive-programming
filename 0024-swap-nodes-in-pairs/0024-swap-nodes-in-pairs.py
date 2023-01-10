# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = []
        temp = head
        while temp != None:
            c.append(temp.val)
            temp = temp.next
        for i in range(0,len(c),2):
            if i == len(c)-1:
                break
            c[i],c[i+1] = c[i+1],c[i]
        temp = head
        for i in range(len(c)):
            temp.val = c[i]
            temp = temp.next
        return head
        