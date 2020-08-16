#### https://leetcode.com/explore/featured/card/top-interview-questions-easy/94/trees/555/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        lTree = self.maxDepth(root.left) + 1
        rTree = self.maxDepth(root.right) + 1

        if lTree > rTree:
            return lTree
        else:
            return rTree
