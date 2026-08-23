import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #dijkstra
        n=len(grid)
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        hp=[]
        heapq.heappush(hp,(grid[0][0],0,0))
        visited=[[False for _ in range(n)] for _ in range(n)]
        visited[0][0]=True
        #instead of keeping track of shortest path sum we change cost function to min value we can see to reach that function--dijkstra gives us the ability to get the next square we can reach greedily.
        while hp:
            el=heapq.heappop(hp)
            if el[1]==n-1 and el[2]==n-1:
                return el[0]
            for x,y in directions:
                p,q=el[1]+x,el[2]+y
                if p<0 or q<0 or p>=n or q>=n or visited[p][q]:
                    continue
                visited[p][q]=True#we wantt o stop pushing for this square as soon as we have found the minimum time to reachb it not when it pops
                heapq.heappush(hp,(max(el[0],grid[p][q]),p,q))
    



