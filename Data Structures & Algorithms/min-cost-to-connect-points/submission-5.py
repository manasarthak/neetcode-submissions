import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #solution 3: next implementation of prim's(optimal): instaed of computing all edges; compute the nearest distance on the fly
        n=len(points)
        min_dist=[float('inf')]*n
        min_dist[0]=0
        seen=[False]*n
        total=0
        for _ in range(n):#each iteration we add one node 
            nxt=-1 #an invalid index as the default
            for idx in range(n):
                if not seen[idx] and (nxt==-1 or min_dist[idx]<min_dist[nxt]):
                    nxt=idx
            seen[nxt]=True
            total+=min_dist[nxt]
            #next we add all the updates to min_dist that happen bcoz we added a node to our MST
            x,y=points[nxt][0],points[nxt][1]
            for idx in range(n):
                if not seen[idx]:
                    dist=abs(points[idx][0]-x)+abs(points[idx][1]-y)
                    if dist<min_dist[idx]:
                        min_dist[idx]=dist
        return total
                