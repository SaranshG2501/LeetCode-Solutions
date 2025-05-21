class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        min_open = 0  # Minimum number of open parentheses
        max_open = 0  # Maximum number of open parentheses
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1  # Treat '*' as ')'
                max_open += 1  # Treat '*' as '('
            
            # Ensure min_open does not go below 0
            if min_open < 0:
                min_open = 0
            
            # If max_open goes negative, we have too many ')'
            if max_open < 0:
                return False
        
        # At the end, min_open should be 0 for the string to be valid
        return min_open == 0
