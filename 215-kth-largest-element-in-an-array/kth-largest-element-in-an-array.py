import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # Transform the list into a heap in O(k) time

        # Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:  # Only add to the heap if the current number is larger than the smallest in the heap
                heapq.heappop(min_heap)  # Remove the smallest element
                heapq.heappush(min_heap, num)  # Add the current number

        # The root of the min-heap is the k-th largest element
        return min_heap[0]
