class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for i in matrix:
            nums = nums + i
        return sorted(nums)[k-1]