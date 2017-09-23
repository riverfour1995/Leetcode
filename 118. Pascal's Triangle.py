class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1]*k for k in range(1, numRows + 1)]
        print(res)
        for i in range(2,numRows):
            print(i)
            for j in range(1,len(res[i]) - 1):
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
        return res