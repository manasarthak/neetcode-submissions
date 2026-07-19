# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        early=[False]
        ans=[-1]
        def dfs(root):
            nonlocal k
            if not root or early[0]:
                return
            dfs(root.left)
            k-=1
            if k==0:
                ans[0]=root.val
                early[0]=True
            dfs(root.right)
            return
        dfs(root)
        return ans[0]
