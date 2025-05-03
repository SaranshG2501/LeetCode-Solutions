# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Move slow pointer by 1
            fast = fast.next.next     # Move fast pointer by 2
            
            if slow == fast:          # If they meet, there is a cycle
                return True
        
        return False                 # If we reach the end, there is no cycle