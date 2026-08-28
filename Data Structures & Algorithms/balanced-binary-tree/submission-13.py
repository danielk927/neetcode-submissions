# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root): 
            if not root: 
                return 0, True

            left, leftBal = dfs(root.left) 
            right, rightBal = dfs(root.right) 
            height = 1 + max(left, right) 
            balanced = leftBal and rightBal and abs(right-left) <= 1 

            return height, balanced
        height, balanced = dfs(root)
        return balanced