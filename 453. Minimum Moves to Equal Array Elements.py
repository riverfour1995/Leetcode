class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sum + (n - 1) * k  =n * m
        # min + k = m
        return sum(nums)-len(nums)*min(nums)