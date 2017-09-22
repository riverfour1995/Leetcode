class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        string = [s for s in str(abs(x))][::-1]

        reverse_x = int(''.join(string))
        print(reverse_x)

        if reverse_x > 2147483647:
            return False

        if reverse_x == abs(x):
            return True
        else:
            return False

A = Solution()
print(A.isPalindrome(-2147447412))