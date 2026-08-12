import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #second method : dijkstra
        adj=[[] for _ in range(n+1)]
        for u,v,t in times:
            adj[u].append((v,t))
        hq=[(0,k)]
        seen=[False]*(n+1)
        next_dist=0
        ans=0
        while hq:
            next_dist,node=heapq.heappop(hq)
            if seen[node]:
                continue
            ans=next_dist
            seen[node]=True
            for nxt_node,add_dist in adj[node]:
                if not seen[nxt_node]:
                    heapq.heappush(hq,(add_dist+next_dist,nxt_node))
        if not all(seen[1:]):
            return -1
        return ans
                    







            
        
        