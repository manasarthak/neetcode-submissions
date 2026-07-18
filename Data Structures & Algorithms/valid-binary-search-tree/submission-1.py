# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[True]
        early=[False]
        def dfs(root,left,right):
            if not root or early[0]:
                return
            if left>=root.val or root.val>=right:
                ans[0]=False
                early[0]=True
            dfs(root.left,left,min(right,root.val))
            dfs(root.right,max(left,root.val),right)
            return
        dfs(root,-1001,1001)
        return ans[0]
            

                

            

            

        