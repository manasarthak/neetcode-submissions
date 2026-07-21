# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=-1001

        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            ans=max(left+root.val,right+root.val,root.val,ans,root.val+left+right)
            return max(0,left+root.val,right+root.val,root.val)
        dfs(root)
        return ans


        