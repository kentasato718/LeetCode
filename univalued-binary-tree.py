# https://leetcode.com/problems/univalued-binary-tree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
root = TreeNode(x)
solution = Solution()
print(solution.isUnivalTree(root))

