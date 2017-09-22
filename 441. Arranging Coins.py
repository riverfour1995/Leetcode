# import math
# # class Solution(object):
# #     def arrangeCoins(self, n):
# #         """
# #         :type n: int
# #         :rtype: int
# #         """
# #
#
# def permutation(lst):
#     res = []
#     if len(lst) == 0:
#         return []
#     elif len(lst) == 1:
#         return [lst]
#     else:
#         for i in range(len(lst)):
#             m = lst[i]
#             remlst = lst[:i] + lst[i+1:]
#             for p in permutation(remlst):
#                 res.append([m]+p)
#     return res
#
# print(permutation([1,3,4]))








