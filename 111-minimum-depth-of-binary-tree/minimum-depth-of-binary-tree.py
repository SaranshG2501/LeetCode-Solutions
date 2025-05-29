# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        
        # If the node is a leaf
        if root.left is None and root.right is None:
            return 1
        
        # If one of the children is None, we only consider the other child
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        # If both children exist, return the minimum of both depths
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1