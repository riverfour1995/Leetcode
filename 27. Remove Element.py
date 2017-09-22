class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [x for x in nums if x != val]
        return len(nums)

A = Solution()
print(A.removeElement([3,2,1,3],3))