# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to help with the merging process
        dummy = ListNode(0)
        current = dummy
        
        # While both lists have nodes to compare
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Link to the smaller node
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2  # Link to the smaller node
                list2 = list2.next     # Move to the next node in list2
            current = current.next     # Move the current pointer forward
        
        # If there are remaining nodes in either list, link them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # The merged list is next to the dummy node
        return dummy.next