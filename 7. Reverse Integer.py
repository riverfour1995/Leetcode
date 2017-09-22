class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if int(''.join([j for j in str(abs(x))][::-1])) > 2147483647:
            return 0
        return int(''.join([i for i in str(x)][::-1])) if x > 0 else - int(''.join([j for j in str(abs(x))][::-1]))

