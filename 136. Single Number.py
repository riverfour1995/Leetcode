import collections
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Set = collections.Counter(nums)
        for key in Set.keys():
            if Set[key] == 1:
                return key


