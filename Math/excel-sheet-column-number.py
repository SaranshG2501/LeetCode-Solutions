class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        length = len(columnTitle)
        
        for i in range(length):
            # Calculate the value of the current character
            value = ord(columnTitle[i]) - ord('A') + 1
            # Update the result, considering the position
            result = result * 26 + value
        
        return result
