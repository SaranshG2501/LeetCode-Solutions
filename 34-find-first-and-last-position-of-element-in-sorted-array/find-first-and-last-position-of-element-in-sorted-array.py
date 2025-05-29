class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1  # continue searching in the left half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1  # continue searching in the right half
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last

        first_position = findFirst(nums, target)
        last_position = findLast(nums, target)

        return [first_position, last_position]

# Example usage:
solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3, 4]
print(solution.searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1, -1]
print(solution.searchRange([], 0))                    # Output: [-1, -1]
