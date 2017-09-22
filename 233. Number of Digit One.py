import collections
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1,n+1):
            number = 0
            if '1' in str(i):
                number = collections.Counter(str(i))['1']
                count = count + number

        return count
A = Solution()
print(A.countDigitOne(3184191))
