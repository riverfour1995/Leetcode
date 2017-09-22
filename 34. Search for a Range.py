class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == []:
            return [-1, -1]
        index = [i for i, j in enumerate(nums) if j == target]

        return [min(index), max(index)]

A = Solution()
print(A.searchRange([1,1,1],1))