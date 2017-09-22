import math as mt
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num  == 1:
            return False
        if num <= 0:
            return False
        divisors = []
        for i in range(1,int(mt.sqrt(num))+1):
            if num%i ==0:
                divisors.append(i)
                divisors.append(int(num/i))
        divisors.remove(num)
        if num == sum(divisors):
            return True
        else:
            return False

A = Solution()
print(A.checkPerfectNumber(28))