

class Solution:
    """
    A class to determine whether you can reach the last index of an integer array `nums`.

    Methods:
        canJump(nums: List[int]) -> bool:
            Returns whether the last index can be reached given the jump lengths.

    Example usage:
        solution = Solution()
        result = solution.canJump([2, 3, 1, 1, 4])  # Returns: True
    """

    def canJump(self, nums: list[int]) -> bool:
        """
        Determines whether you can reach the last index of the array.

        Args:
            nums (List[int]): A list of non-negative integers where each element
                represents your maximum jump length at that position.

        Returns:
            bool: True if you can reach the last index, False otherwise.

        Examples:
            >>> solution = Solution()
            >>> solution.canJump([2, 3, 1, 1, 4])
            True
            >>> solution.canJump([3, 2, 1, 0, 4])
            False

        Constraints:
            1 <= nums.length <= 10^4
            0 <= nums[i] <= 10^5
        """
        momentum = 0

        for step in nums[:-1]:
            momentum = max(momentum, step)
            if momentum <= 0:
                return False
            momentum -= 1
        return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()
