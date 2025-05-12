# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case: if the list is empty or has only one node
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        prev = None
        
        # Traverse the list to find the middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Remove the middle node
        if prev:
            prev.next = slow.next
        
        return head
