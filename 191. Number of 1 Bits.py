import collections
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.value = n
        A = collections.Counter(list(bin(self.value)[2:]))
        return A['1']

A = Solution()
print(A.hammingWeight(1241))