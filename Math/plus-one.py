class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Start from the last digit and work backwards
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Set current digit to 0 if it was 9
        
        # If we exit the loop, it means we had a carry out of the most significant digit
        return [1] + digits  # Prepend 1 to the list