# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        total = 0
        
        # Check if the left child is a leaf node
        if root.left and root.left.left is None and root.left.right is None:
            total += root.left.val
        else:
            # Otherwise, recurse on the left subtree
            total += self.sumOfLeftLeaves(root.left)
        
        # Recurse on the right subtree (no need to check leaf condition here)
        total += self.sumOfLeftLeaves(root.right)
        
        return total
