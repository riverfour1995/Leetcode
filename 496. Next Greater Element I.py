class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in findNums:
            if num >= max(nums[nums.index(num):]):
                res.append(-1)
            for i in range(nums.index(num)+1,len(nums)):
                if nums[i] > num:
                    res.append(nums[i])
                    break

        return res
A = Solution()
print(A.nextGreaterElement([4,1,2],[1,3,4,2]))