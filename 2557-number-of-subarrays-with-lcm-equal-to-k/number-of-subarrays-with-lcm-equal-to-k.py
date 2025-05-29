class Solution(object):
    def subarrayLCM(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        count = 0
        n = len(nums)

        for i in range(n):
            current_lcm = 1
            for j in range(i, n):
                current_lcm = lcm(current_lcm, nums[j])
                if current_lcm > k:  # No need to continue if LCM exceeds k
                    break
                if current_lcm == k:
                    count += 1

        return count
