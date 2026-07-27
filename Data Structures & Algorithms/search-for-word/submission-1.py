class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        flag=[False]
        black = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        def bt(i,j,idx):
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or flag[0] or black[i][j]:
                return
            if board[i][j]!=word[idx]:
                return
            if board[i][j]==word[idx] and idx==len(word)-1:
                flag[0]=True
                return
            else:
                black[i][j]=True
                bt(i+1,j,idx+1)
                bt(i,j+1,idx+1)
                bt(i-1,j,idx+1)
                bt(i,j-1,idx+1)
                black[i][j]=False
                return

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    bt(i,j,0)
                if flag[0]:
                    return True
        return False
        