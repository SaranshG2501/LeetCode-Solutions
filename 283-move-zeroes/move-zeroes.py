class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero_index = 0
        
        # Move all non-zero elements to the front of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_index] = nums[i]
                last_non_zero_index += 1
        
        # Fill the remaining positions with zeros
        for i in range(last_non_zero_index, len(nums)):
            nums[i] = 0
