

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.s = 0
        
#gives result of every possible sum 
def sum_path(node, sum_val, node_chain=None):
    if not node_chain:
        node_chain=[]
    if not node:
        return []
    s=0
    res=[]
    node_chain_tmp =  [node.data] + node_chain
    for i, val in enumerate(node_chain_tmp):
       s=s+val
       if s==sum_val:
           solution=(node_chain_tmp[:i+1])
           solution.reverse()
           res.append(solution)
    return res + sum_path(node.left, sum_val, node_chain_tmp) + sum_path(node.right, sum_val, node_chain_tmp)

#root to leaf if sum exists
def csum(node,sum_val):
    if node is None:
        return sum == 0
    else:
        ans = False
        subsum = sum_val - node.data
        if subsum==0 and node.left is None and node.right is  None:
            return True
        if node.left is not None:
            ans = ans or csum(node.left,subsum)
        if node.right is not None:
            ans = ans or csum(node.right,subsum)
        return ans



n1 = TreeNode(3)
n1.left = TreeNode(2)
n1.right = TreeNode(4)
n1.right.left = TreeNode(1)
n1.right.left.left = TreeNode(3)
n1.left.left = TreeNode(3)
n1.left.right = TreeNode(2)
n1.left.left.left = TreeNode(-2)
n1.left.left.right = TreeNode(2)
n1.left.left.left.left = TreeNode(2)


print sum_path(n1, 8, node_chain=None)
print csum(n1,11)
