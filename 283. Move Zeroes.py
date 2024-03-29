class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for num in nums:
        #     if num == 0:
        #         nums.pop(nums.index(0))
        #         nums.append(0)
        #     else:
        #         pass
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1