import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        set = collections.Counter(s)
        return ''.join([n * m for m, n in sorted([(k, j) for j, k in list(zip(set.keys(), set.values()))], reverse=-1)])
