from typing import Optional
class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head: ListNode):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            if fast.next.next:
                fast = fast.next.next
            else: fast = fast.next
        slow = self.reverseList(slow)
        fast = head

        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True
