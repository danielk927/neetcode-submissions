# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0 

        self.longestPath = 0

        def dfs(node): 
            if node == None:
                return 0 
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right) 

            self.longestPath = max(self.longestPath, leftHeight + rightHeight)
    
            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return self.longestPath
            
        
        