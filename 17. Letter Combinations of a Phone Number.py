class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {'1': '*', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                '9': 'wxyz', '0': ' '}
        res_1 = [dict[string] for string in digits]
        print(list(enumerate(res_1)))
        res_2 = []
        res_3 = []
        for m,n in list(enumerate(res_1)):
            i = 0
            while i < len(n):
                res_2.append(n[i])
                i += 1
            res_3.append(res_2)
        print(res_2)
        print(res_3)



A = Solution()
print(A.letterCombinations('21'))
