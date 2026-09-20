# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        
        def dfs(node, currentSum):
            if node is None:
                return False
            
            
            currentSum += node.val
            
            
            if node.left is None and node.right is None: # if leaf node tou check whether current equals target
                return currentSum == targetSum
            
           
            left  = dfs(node.left,  currentSum)
            right = dfs(node.right, currentSum)
            
            return left or right
        
        return dfs(root, 0)
