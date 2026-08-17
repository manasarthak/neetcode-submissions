import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #third method bellman-ford
        inf=float('inf')
        time=[inf]*(n+1)
        time[k]=0
        no_change=False
        for _ in range(n):
            #at most any path will have n-1 edges
            if no_change:
                break
            no_change=True
            for u,v,t in times:
                if time[u]!= inf and time[u]+t<time[v]:
                    time[v]=time[u]+t
                    no_change=False
        if max(time[1:])==inf:
            return -1
        else:
            return max(time[1:])







            
        
        