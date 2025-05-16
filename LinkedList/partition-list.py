# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Create two dummy nodes to help with the partitioning
        less_head = ListNode(0)  # Dummy head for the 'less than x' list
        greater_head = ListNode(0)  # Dummy head for the 'greater than or equal to x' list
        
        less = less_head  # Pointer for the 'less than x' list
        greater = greater_head  # Pointer for the 'greater than or equal to x' list
        
        # Traverse the original list and partition it
        current = head
        while current:
            if current.val < x:
                less.next = current  # Add to the 'less than x' list
                less = less.next
            else:
                greater.next = current  # Add to the 'greater than or equal to x' list
                greater = greater.next
            current = current.next
        
        # Connect the two lists
        greater.next = None  # End the 'greater than or equal to x' list
        less.next = greater_head.next  # Connect the 'less than x' list to the 'greater' list
        
        return less_head.next  # Return the head of the new partitioned list
