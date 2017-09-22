class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        length = len(grid[0])
        width = len(grid)

        expand_grid = [[0] * (length + 2) for k in range(width + 2)]
        for m in range(width):
            for n in range(length):
                expand_grid[m + 1][n + 1] = grid[m][n]

        res = 0
        for j in range(1, width + 1):
            for k in range(1, length + 1):
                res_1 = 4
                if expand_grid[j][k] == 1:
                    if expand_grid[j + 1][k] == 1:
                        # print('a')
                        res_1 -= 1
                    if expand_grid[j][k + 1] == 1:
                        # print('b')
                        res_1 -= 1
                    if expand_grid[j - 1][k] == 1:
                        # print('c')
                        res_1 -= 1
                    if expand_grid[j][k - 1] == 1:
                        # print('d')
                        res_1 -= 1
                    print(res_1)
                    res += res_1
        return res

A = Solution()
print(A.islandPerimeter([[1,0]]))