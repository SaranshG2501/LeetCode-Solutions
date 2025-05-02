# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next        # Move slow pointer by 1
            fast = fast.next.next   # Move fast pointer by 2
        
        return slow  # When fast reaches the end, slow will be at the middle