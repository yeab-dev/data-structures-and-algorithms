from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headNode = head
        currentNode = head
        while currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            currentNode = currentNode.next
        return headNode