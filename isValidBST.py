# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
INT_MAX = sys.maxint
INT_MIN = -1 - sys.maxint

class BinaryTree:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None


class Solution(object):
    def isvalidBSThelper(self, root, min, max):
        if root is None:
            return True
        if (root is not None and root.val < min) or (root is not None and root.val > max):
            return False
        return (self.isvalidBSThelper(root.left, min, root.val-1) and self.isvalidBSThelper(root.right, root.val+1, max))


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        print self.isvalidBSThelper(root, INT_MIN, INT_MAX)

if __name__ == "__main__":
    s = Solution()
    b = BinaryTree(4)
    b.right = BinaryTree(5)
    b.left = BinaryTree(2)
    # b.left.left = BinaryTree(4)
    # b.left.right = BinaryTree(5)
    s. isValidBST(b)
