class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        rows,cols=len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j>=cols or board[i][j]=='X' or board[i][j]=='_':
                return
            board[i][j]='_'
            for m,n in directions:
                x,y=i+m,j+n
                dfs(x,y)
            return
        for i in range(rows):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][cols-1]=='O':
                dfs(i,cols-1)
        for j in range(cols):
            if board[0][j]=='O':
                dfs(0,j)
            if board[rows-1][j]=='O':
                dfs(rows-1,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='_':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

        