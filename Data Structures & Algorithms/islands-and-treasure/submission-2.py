class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(i,j):
            x,y=i,j
            depth=0
            visited=[[None for _ in range(len(grid[0]))] for _ in range(len(grid))]
            queue=deque([[i,j]])
            visited[i][j]=True
            while queue and grid[x][y]==2147483647:
                z=len(queue)
                for i in range(z):
                    el=queue.popleft()
                    m,n=el[0],el[1]
                    if grid[m][n]==0:
                        grid[x][y]=depth
                        break
                    else:
                        if m>0 and grid[m-1][n]!=-1 and not visited[m-1][n]:
                            queue.append([m-1,n])
                            visited[m-1][n]=True
                        if n>0 and grid[m][n-1]!=-1 and not visited[m][n-1]:
                            queue.append([m,n-1])
                            visited[m][n-1]=True
                        if m<len(grid)-1 and grid[m+1][n]!=-1 and not visited[m+1][n]:
                            queue.append([m+1,n])
                            visited[m+1][n]=True
                        if n<len(grid[0])-1 and grid[m][n+1]!=-1 and not visited[m][n+1]:
                            queue.append([m,n+1])
                            visited[m][n+1]=True
                depth+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2147483647:
                    bfs(i,j)
        