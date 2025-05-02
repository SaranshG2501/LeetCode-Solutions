class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        
        # Initialize the sum of divisors
        sum_of_divisors = 0
        
        # Iterate through possible divisors
        for i in range(1, int(num**0.5) + 1):
            if num % i == 0:  # If i is a divisor
                sum_of_divisors += i
                if i != 1 and i != num // i:  # Avoid adding the number itself and duplicates
                    sum_of_divisors += num // i
        
        return sum_of_divisors == num