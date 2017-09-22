class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first_row = 'qwertyuiopQWERTYUIOP'
        second_row = 'asdfghjklASDFGHJKL'
        third_row = 'zxcvbnmZXCVBNM'

        res = []
        for word in words:
            if set(word) <= set(first_row) or set(word) <= set(second_row) or set(word) <= set(third_row):
                res.append(word)
        return res

A = Solution()
print(A.findWords(["Hello","Alaska","Dad","Peace"]))