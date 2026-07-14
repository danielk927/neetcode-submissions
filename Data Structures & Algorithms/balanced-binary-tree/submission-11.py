# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True 
        def dfs(root): 
            if root == None: 
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right) 

            if left[0] == True and right[0] == True and abs(left[1] - right[1]) <= 1: 
                balanced = True
            else:
                balanced = False

            height = 1 + max(left[1], right[1]) 
            return [balanced, height]
        return dfs(root)[0]