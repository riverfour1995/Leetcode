class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str = set([(a,b) for (a,b) in zip(s,t)])
        if len(set(i[0] for i in str))==len(set(i[1] for i in str))==len(str):
            return True
        else:
            return False

A = Solution()
print(A.isIsomorphic('',''))