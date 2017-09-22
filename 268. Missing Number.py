class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.value = nums
        number = len(self.value) + 1
        whole_list = list(range(number))
        return int(list(set(whole_list)-set(self.value))[0])

#set can be used to substract
