class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        num_set = set(nums)
        for i in range(n + 1):
            if i not in num_set:
                return i
        