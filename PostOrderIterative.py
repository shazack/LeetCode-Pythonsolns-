# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def peek(stack):
            if len(stack)>0:
                return stack[-1]
            else:
                return None
        stack = []
        soln = []
        
        if root is None:
            return []
    
        current = root
        while(True):
            while current is not None:
                if current.right is not None:
                    stack.append(current.right)
                stack.append(current)
                current = current.left
            current = stack.pop()
            if current.right is not None and current.right == peek(stack):
                stack.pop()
                stack.append(current) 
                current = current.right
            else:
                soln.append(current.val)
                current = None
            if len(stack)<=0:
                break
        return soln
