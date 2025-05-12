# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Start with the head of the list
        current = head
        
        # Traverse the linked list
        while current and current.next:
            # Calculate GCD of current node and the next node
            g = gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(g)
            
            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
            # Move to the next pair (skip the newly inserted node)
            current = new_node.next
        
        return head
