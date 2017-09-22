class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1
        width = len(matrix)

        while col >= 0 and row < width:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col = col - 1
            else:
                row = row + 1
        return False

A=Solution()
print(A.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],23))

