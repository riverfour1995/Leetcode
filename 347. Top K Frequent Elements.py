import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        set = dict(collections.Counter(nums))

        return [n for m, n in sorted([(i, j) for j, i in list(zip(set.keys(), set.values()))], reverse=-1)][:k]


A = Solution()
print(A.topKFrequent([1,1,1,2,2,3],2))





