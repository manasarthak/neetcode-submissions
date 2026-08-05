class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        rows,cols=len(grid),len(grid[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append([i,j])
        depth=0
        inf=2147483647
        while queue:
            ln=len(queue)
            for i in range(ln):
                m,n=queue.popleft()
                if grid[m][n]==inf:
                    grid[m][n]=depth
                
                for direction in directions:
                    x,y=m+direction[0],n+direction[1]
                    if x>=0 and y>=0 and x<rows and y<cols and grid[x][y]==inf:
                        queue.append([x,y])
            depth+=1
        




        