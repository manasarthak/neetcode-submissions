# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans=root
        if p.val>q.val:
            p,q=q,p
        while True:
            if p.val<=ans.val and q.val>=ans.val:
                return ans
            elif q.val<ans.val:
                ans=ans.left
            else:
                ans=ans.right
        