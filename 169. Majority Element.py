import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set = collections.Counter(nums)
        zip_set = list(zip(set.keys(), set.values()))
        return [m for m, n in zip_set if n > round(len(nums) / 2)][0]

        # return sorted(num)[len(num)/2]
