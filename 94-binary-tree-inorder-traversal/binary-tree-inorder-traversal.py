class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []
        current = root
        
        while current is not None or stack:
            # Traverse to the leftmost node
            while current is not None:
                stack.append(current)  # Push current node to stack
                current = current.left  # Move to left child
            
            current = stack.pop()      # Pop from stack
            result.append(current.val)  # Visit node
            current = current.right     # Move to right child
        
        return result

# Example usage:
# Constructing the binary tree for the first example
#       1
#        \
#         2
#        /
#       3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]
