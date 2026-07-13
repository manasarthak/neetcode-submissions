# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans=0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            height_l=1+dfs(root.left)
            height_r=1+dfs(root.right)
            ans=max(ans,height_l+height_r-2)
            return max(height_l,height_r)
        dfs(root)
        return ans
        