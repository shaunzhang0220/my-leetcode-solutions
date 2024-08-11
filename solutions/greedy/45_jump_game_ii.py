

class Solution:
    """A class to solve the problem of finding the minimum number of jumps needed to reach the last
    index in an integer array `nums`.
    """

    def jump(self, nums: list[int]):
        """Calculates the minimum number of jumps to reach the last index of the array.

        Args:
            nums: A list of non-negative integers where each element represents the maximum length
                of a forward jump from that position.

        Returns:
            The minimum number of jumps required to reach the last index.

        Examples:
            >>> solution = Solution()
            >>> solution.jump([2, 3, 1, 1, 4])
            2
            >>> solution.jump([2, 3, 0, 1, 4])
            2

        Constraints:
            1 <= nums.length <= 10^4
            0 <= nums[i] <= 10^5
        """
        jumps = relay_station = farthest = 0
        destination = len(nums) - 1

        for i in range(destination):
            farthest = max(farthest, i + nums[i])
            if i == relay_station:
                jumps += 1
                relay_station = farthest
                if relay_station >= destination:
                    break
        
        return jumps


if __name__ == "__main__":
    import doctest
    doctest.testmod()
