class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find the smallest and largest numbers in the array
        smallest = min(nums)
        largest = max(nums)
        
        # Function to compute GCD using the Euclidean algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # Return the GCD of the smallest and largest numbers
        return gcd(smallest, largest)
