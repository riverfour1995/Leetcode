class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        self.a = list(bin(x))[2:]
        self.b = list(bin(y))[2:]
        length = max(len(self.a),len(self.b))
        self.a = ['0']*(length-len(self.a))+self.a
        self.b = ['0']*(length-len(self.b))+self.b
        count = 0
        for i in range(length):
            if self.a[i]!=self.b[i]:
                count = count + 1

        return count


A = Solution()
print(A.hammingDistance(1,4))


