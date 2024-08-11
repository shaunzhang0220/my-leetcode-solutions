

class Solution:
    """
    A class used to determine if a given positive integer is a perfect square.

    A perfect square is an integer that is the square of another integer, i.e., 
    it is the product of some integer with itself. The algorithm does not use 
    any built-in library functions like sqrt.

    Methods:
        isPerfectSquare(num: int) -> bool:
            Returns True if the given integer is a perfect square, False otherwise.

    Example usage:
        solution = Solution()
        result = solution.isPerfectSquare(16)  # Returns: True
    """

    def isPerfectSquare(self, num: int):
        """
        Determines if the given positive integer is a perfect square.

        Args:
            num (int): A positive integer to check if it is a perfect square.

        Returns:
            bool: True if the given integer is a perfect square, False otherwise.

        Examples:
            >>> solution = Solution()
            >>> solution.isPerfectSquare(16)
            True
            >>> solution.isPerfectSquare(14)
            False

        Constraints:
            1 <= num <= 2^31 - 1
        """
        left, right = 0, num

        while left <= right:
            mid = (left + right) // 2

            square = mid ** 2
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()

