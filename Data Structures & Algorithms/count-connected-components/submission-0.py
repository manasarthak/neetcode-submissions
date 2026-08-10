class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen=set()
        adj=[[] for _ in range(n)]
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        def dfs(i):
            if i in seen:
                return
            seen.add(i)
            for j in adj[i]:
                dfs(j)
            return
        ans=0
        for n in range(n):
            if n not in seen:
                dfs(n)
                ans+=1
        return ans
        