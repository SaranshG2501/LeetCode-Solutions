class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Step 1: Determine the number of digits
        digit_length = 1  # Start with 1-digit numbers
        count = 9  # There are 9 one-digit numbers
        start = 1  # The first number with 'digit_length' digits
        
        # Step 2: Find the range where n falls
        while n > digit_length * count:
            n -= digit_length * count
            digit_length += 1
            count *= 10
            start *= 10
        
        # Step 3: Find the actual number
        start += (n - 1) // digit_length  # Find the actual number
        number_str = str(start)  # Convert to string to access digits
        
        # Step 4: Find the specific digit
        index = (n - 1) % digit_length  # Find the index of the digit in the number
        return int(number_str[index])  # Return the digit as an integer
