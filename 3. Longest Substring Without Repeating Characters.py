class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sub_string = [len(s[x:y]) for x in range(len(s)+1) for y in range(len(s)+1) if s[x:y] !='' and len(s[x:y]) == len(set(s[x:y]))]

        # print(sub_string)
        # return 0 if sub_string == [] else max(sub_string)
        res = []
        string = ''
        for stri in s:
            string += stri
            if len(string) == len(set(string)):
                res.append(string)
                pass
            else:
                string = string[1:]

        return max([len(s) for s in res]) if [len(s) for s in res] != [] else 0
