# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        st = []
        linkedList = []
        indexNextGreatestPair = defaultdict(int)
        
        
        while head :
            linkedList.append(head.val)
            head = head.next
        

        for i in range(len(linkedList)):
            while st and linkedList[st[-1]] < linkedList[i]:
                index = st.pop()
                indexNextGreatestPair[index] = linkedList[i]
                
            st.append(i)
            
        for i in range(len(linkedList)):
            if i in indexNextGreatestPair:
                linkedList[i] = indexNextGreatestPair[i]
            else:
                linkedList[i] = 0
            
        
        return linkedList