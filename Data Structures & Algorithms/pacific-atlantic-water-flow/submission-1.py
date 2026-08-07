class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        rows,cols=len(heights),len(heights[0])
        ans=[]
        pacific=set()
        atlantic=set()
        def dfs(i,j,copy):
            copy.add((i,j))
            for m,n in directions:
                x,y=i+m,j+n
                if x<0 or y<0 or x>=rows or y>=cols or (x,y) in copy:
                    continue
                elif heights[x][y]>=heights[i][j]:
                    dfs(x,y,copy)
            return
        for i in range(rows):
            dfs(i,0,pacific)
            dfs(i,cols-1,atlantic)
        for i in range(cols):
            dfs(0,i,pacific)
            dfs(rows-1,i,atlantic)
        #print(pacific,atlantic)
        for m,n in pacific:
            if (m,n) in atlantic:
                ans.append([m,n])
        return ans

        