class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set([i+1 for i in range(len(nums))]) - set(nums))

A = Solution()
print(A.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
