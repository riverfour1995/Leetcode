# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = 0
        self.result = 0

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder_traverse(root, k)
        return self.result

    def inorder_traverse(self, root, k):
        if not root:
            return
        self.inorder_traverse(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
        self.inorder_traverse(root.right, k)