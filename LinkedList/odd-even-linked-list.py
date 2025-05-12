# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        odd = head  # Head of the odd indexed nodes
        even = head.next  # Head of the even indexed nodes
        even_head = even  # Keep the head of the even indexed nodes to connect later
        
        while even and even.next:
            odd.next = even.next  # Link the current odd node to the next odd node
            odd = odd.next  # Move the odd pointer to the next odd node
            even.next = odd.next  # Link the current even node to the next even node
            even = even.next  # Move the even pointer to the next even node
        
        odd.next = even_head  # Connect the end of odd indexed list to the head of even indexed list
        
        return head  # Return the head of the modified list
