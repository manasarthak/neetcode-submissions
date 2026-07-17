# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        temp=[]
        if not root:
            return ans
        temp.append(root)
        while temp:
            temp2=[]
            temp1=[]
            for i in range(0,len(temp)):
                el=temp[i]
                temp1.append(el.val)
                if el.left:
                    temp2.append(el.left)
                if el.right:
                    temp2.append(el.right)
            temp=temp2
            ans.append(temp1)
        return ans


        