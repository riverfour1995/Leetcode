class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        length = len(matrix[0])
        width = len(matrix)

        m = 0
        n = length - 1

        while n >= 0 and m <= width - 1:
            if matrix[m][n] > target:
                n -= 1
            elif matrix[m][n] < target:
                m += 1
            else:
                return True
        return False

