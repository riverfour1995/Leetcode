import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        reverse_s = ''.join([i for i in s][::-1])
        s_char = [k.lower() for k in s if k.isalnum() or k.isalpha()]
        reverse_s_char = [k.lower() for k in reverse_s if k.isalpha() or k.isalnum()]
        print(s_char)
        print(reverse_s_char)
        if ''.join([m for m in s_char]) == ''.join([n for n in reverse_s_char]):
            return True
        else:
            return False

A= Solution()
print(A.isPalindrome('0P'))