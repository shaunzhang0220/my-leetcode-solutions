

class Solution:
    """A class to calculate the h-index of a researcher based on their citation count.

    The h-index is defined as the maximum value of h such that the given researcher
    has published at least h papers that have each been cited at least h times. The
    citations are provided in a sorted array, and the algorithm is designed to run
    in logarithmic time.

    Methods:
        hIndex(citations: List[int]) -> int:
            Returns the researcher's h-index.

    Example usage:
        solution = Solution()
        result = solution.hIndex([0, 1, 3, 5, 6])  # Returns: 3
    """

    def hIndex(self, citations: list[int]):
        """Determines the h-index for a researcher given their citation counts.

        Args:
            citations (List[int]): A sorted list of non-negative integers where 
                each element represents the number of citations for a particular paper.

        Returns:
            int: The h-index of the researcher.

        Examples:
            >>> solution = Solution()
            >>> solution.hIndex([0, 1, 3, 5, 6])
            3
            >>> solution.hIndex([1, 2, 100])
            2

        Constraints:
            1 <= len(citations) <= 10^5
            0 <= citations[i] <= 1000
        """
        left, right = 0, len(citations) - 1
        while left <= right:
            mid = (left + right) // 2
            h_index = len(citations) - mid

            if citations[mid] == h_index:
                return h_index
            elif citations[mid] > h_index:
                right = mid - 1
            else:
                left = mid + 1
        return len(citations) - left


if __name__ == "__main__":
    import doctest
    doctest.testmod()
