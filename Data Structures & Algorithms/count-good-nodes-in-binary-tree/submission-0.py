# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=[0]
        def dfs(root,m_seen):
            if not root:
                return
            if root.val>=m_seen:
                ans[0]+=1
            m_seen=max(m_seen,root.val)
            dfs(root.left,m_seen)
            dfs(root.right,m_seen)
            return
        dfs(root,-101)
        return ans[0]
            

        