import collections
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        set = collections.Counter(nums)
        for i in range(set[0]):
            nums[i] = 0
        for j in range(set[0], set[0] + set[1]):
            nums[j] = 1
        for k in range(set[0] + set[1], set[0] + set[1] + set[2]):
            nums[k] = 2

