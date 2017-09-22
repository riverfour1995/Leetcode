class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(len(i) for i in ''.join([str(i) for i in nums]).split('0'))