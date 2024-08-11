

class Solution:
    """A class to solve the problem of finding the shortest unsorted continuous subarray.
    
    Example usage:
        solution = Solution()
        result = solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])  # Expected output: 5
    """

    def findUnsortedSubarray(self, nums: list[int]) -> int:
        """Finds the length of the shortest continuous subarray that, if sorted, results in the entire array being sorted.
        
        Args:
            nums: A list of integers.
        
        Returns:
            The length of the shortest such subarray.
        
        Examples:
            >>> solution = Solution()
            >>> solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
            5
            >>> solution.findUnsortedSubarray([1, 2, 3, 4])
            0
            >>> solution.findUnsortedSubarray([1])
            0
        
        Constraints:
            1 <= nums.length <= 10^4
            -10^5 <= nums[i] <= 10^5
        """
        n = len(nums)
        start, end = -1, -1
        max_seen, min_seen = -100001, 100001

        # Traverse from left to right to find the end of the unsorted subarray
        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                end = i

        # Traverse from right to left to find the start of the unsorted subarray
        for i in range(n - 1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                start = i

        if start == -1 and end == -1:
            return 0  # The array is already sorted

        return end - start + 1


        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
