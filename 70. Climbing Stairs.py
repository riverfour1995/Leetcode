class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        a, b = 1,2
        for i in range(3,n+1):
            c = a + b
            a = b
            b = c
        return b

A = Solution()
print(A.climbStairs(4))
