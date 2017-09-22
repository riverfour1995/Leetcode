class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [nums[x:y] for x in range(len(nums)+1) for y in range(len(nums)+1) if nums[x:y] != []]
        res.append([])
        return res

A = Solution()
print(A.subsets([1,2,3]))