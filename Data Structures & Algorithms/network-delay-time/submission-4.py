class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #fourth method: floyd warshall
        time=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        for u,v,t in times:
            time[u][v]=t
        for i in range(1, n+1):
            time[i][i] = 0
        for z in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    time[i][j]=min(time[i][j],time[i][z]+time[z][j])
        mx=0
        print(time)
        for m in range(1,n+1):
            if time[k][m]==float('inf') and k!=m:
                return -1
            else:
                mx=max(mx,time[k][m])
        return mx
            
        







            
        
        