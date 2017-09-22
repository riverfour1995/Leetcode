class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binary = str(bin(num))[2:]
        res = ''
        for i in binary:
            if i =='1':
                i = '0'
                res = res + i
            else:
                i = '1'
                res = res + i

        return int(str(res),2)


A = Solution()
print(A.findComplement(1))