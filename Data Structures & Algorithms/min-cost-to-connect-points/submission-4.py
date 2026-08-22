import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #solution 2: start from arbitrary point-> get the cheapest edge at each point as long as the next point is not in the mst.(cut property between tree and rest of the points.) prereqq here would be a weighted adjacency list
        n=len(points)
        adj=[[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        heap=[]
        seen=[False]*n
        heapq.heappush(heap,(0,0))
        cnt=0
        total=0
        while cnt<n:
            el=heapq.heappop(heap)
            if seen[el[1]]:
                continue
            cnt+=1
            total+=el[0]
            seen[el[1]]=True
            for avl in adj[el[1]]:
                heapq.heappush(heap,avl)
        return total

        
        