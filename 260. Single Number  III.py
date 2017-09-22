import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        set = collections.Counter(nums)
        return [k for k, j in zip(set.keys(), set.values()) if j == 1]

