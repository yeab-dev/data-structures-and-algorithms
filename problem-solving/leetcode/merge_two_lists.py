from typing import Optional
class ListNode:
    def __init__(self, val=0, next= None):
        self.val = val
        self.next = next
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = ListNode()
        head = currentNode
        while list1 and list2:
            if(list1.val < list2.val):
                currentNode.next = ListNode(list1.val)
                currentNode = currentNode.next
                list1 = list1.next
                
            else:
                currentNode.next = ListNode(list2.val)
                currentNode = currentNode.next
                list2 = list2.next
        if list1:
           currentNode.next = list1
        if list2:
           currentNode.next = list2 
        return head.next