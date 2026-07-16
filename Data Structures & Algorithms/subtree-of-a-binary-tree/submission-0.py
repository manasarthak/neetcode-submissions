# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_eq(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val!=node2.val:
                return False
            return True and check_eq(node1.left,node2.left) and check_eq(node1.right,node2.right)
        queue = [root]
        flag=False
        while queue:
            temp=queue.pop()
            print(temp.val)
            if temp.val==subRoot.val:
                flag=check_eq(temp,subRoot)
            if flag:
                return True
            else:
                if temp.right:
                    queue.append(temp.right)
                if temp.left:
                    queue.append(temp.left)
        return False
                
        
            
        