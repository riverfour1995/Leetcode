import collections
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_s = collections.Counter(s)
        dict_t = collections.Counter(t)
        return [i for i in dict_t.keys() if dict_t[i]-dict_s[i] == 1][0]