class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj={}
        for src,dst in edges:
            adj.setdefault(src, []).append(dst)
            adj.setdefault(dst, []).append(src)
        #assuming all nodes connected and no cycles for a valid tree
        on_stack=set()
        flag=[False]
        def dfs(par,i):
            if i in on_stack:
                return False
            on_stack.add(i)
            if i not in adj:
                return True
            

            for j in adj[i]:
                if j==par:
                    continue
                if not dfs(i,j):
                    return False
            return True
        return dfs(-1,0) and len(on_stack)==n

        