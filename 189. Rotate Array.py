class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        nums[:] = nums[length - k:] + nums[:length - k]


A = Solution()
A.rotate([1,2,3,4,5,6,7],3)