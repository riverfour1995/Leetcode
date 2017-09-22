class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits == [0]:
            return [1]
        num = int(''.join(tuple(str(j) for j in digits)))
        num += 1
        return [int(i) for i in str(num)]

A = Solution()
print(A.plusOne([1,2]))