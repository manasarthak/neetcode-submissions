class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(len(edges)+1)]
        for edg in edges:
            adj[edg[0]].append(edg[1])
            adj[edg[1]].append(edg[0])
        cycle=set()
        on_stack=set()
        path=[]
        def dfs(src,dst):
            if dst in on_stack:
                cycle.update(path[path.index(dst):])
                return True
            on_stack.add(dst)
            path.append(dst)
            for j in adj[dst]:
                if j!=src:
                    if dfs(dst,j):
                        return True
            on_stack.discard(dst)
            path.pop()
            return False
        dfs(-1,1)
        for i in range(len(edges)-1,-1,-1):
            if edges[i][0] in cycle and edges[i][1] in cycle:
                return [edges[i][0],edges[i][1]]

        