class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        set = list(enumerate(s))
        length = len(s) - 1
        return sum([pow(26,length-k)*(ord(j)-64) for k,j in set])


print(Solution().titleToNumber('AA'))

