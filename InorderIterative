class BinaryTree:
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None

class Traversal:
    def __init__(self,head):
        self.head = head
    def inorder(self,head):
        current = head
        done = 0
        stack = []
        while not done:
            while current is not None:
                stack.append(current)
                current = current.left
            if current is None and len(stack)>0:
                    top = stack.pop()
                    print top.key
                    current = top.right
            if current is None and len(stack) == 0:
                done = 1
