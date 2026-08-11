class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for _ in range(n+1)]
        cost=[[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append(v)
            cost[u].append(t)
        min_time=[float('inf')]*(n+1)
        def dfs(i,time):
            if time >= min_time[i]:
               return              # no improvement, prune
            min_time[i] = time  
            for j in range(len(adj[i])):
                dfs(adj[i][j],time+cost[i][j])
            return
        dfs(k,0)
        ans=max(min_time[1:])
        if ans==float('inf'):
            return -1
        else:
            return ans


            
        
        