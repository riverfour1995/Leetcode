import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if set(ransomNote) <= set(magazine):
            res_1 = {}
            for i in list(set(ransomNote)):
                count = 0
                for j in ransomNote:
                    if j == i:
                        count = count + 1
                res_1[i] = count

            print(res_1)

            res_2 = {}
            for i in list(set(magazine)):
                count = 0
                for j in magazine:
                    if j == i:
                        count = count + 1
                res_2[i] = count
            print(res_2)

            result = 1
            for i in res_1.keys():
                if (res_1[i]>res_2[i]):
                    result = result * 0
                else:
                    result = result * 1
            return bool(result)

        else:
            print('a')
            return bool(0)

#answer
def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)



A=Solution()
print(A.canConstruct('aa','aab'))
print(list(set('aa')))
print(list(set('aab')))



