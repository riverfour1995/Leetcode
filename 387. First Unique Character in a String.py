import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # set = collections.Counter(s)
        # if 1 not in set.values():
        # return -1
        # for word in s:
        # if set[word] == 1:
        # return s.index(word)
        # break

        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])





