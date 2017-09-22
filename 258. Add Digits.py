class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return sum([int(k) for k in str(num)]) if len([int(k) for k in str(num)]) == 1 else Solution.addDigits(self,int(''.join([str(i) for i in [int(j) for j in str(sum([int(k) for k in str(num)]))]])))


A = Solution()
print(A.addDigits(38))
