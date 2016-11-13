class BinaryTree:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

class Traversal:
    def __init__(self,head):
        self.head = head
        
    def preorder(self,root):
        curr = root
        stack = []
        stack.append(root)
        while len(stack)>0:
            top = stack.pop()
            print top.key
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
