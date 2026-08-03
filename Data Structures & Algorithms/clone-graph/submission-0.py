"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        mp={node:Node(node.val)}
        dq=deque([node])
        while dq:
            el=dq.popleft()
            for nei in el.neighbors:
                if nei not in mp:
                    mp[nei]=Node(nei.val)
                    dq.append(nei)
                mp[el].neighbors.append(mp[nei])
        return mp[node]            



        