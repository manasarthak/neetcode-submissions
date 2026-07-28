class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        temp=[ [ None for i in range(n)] for i in range(n)]   
        ans=[]
        def bt(idx):
            nonlocal temp
            if idx==n:
                ans.append([''.join(arr) for arr in temp])
                return
            for i in range(0,n):
                if not temp[idx][i]:
                    snapshot=[row[:] for row in temp]
                    temp[idx][i]='Q'
                    for j in range(n):
                        if not temp[idx][j]:
                            temp[idx][j]='.'
                        if not temp[j][i]:
                            temp[j][i]='.'
                        if idx-j>-1 and i-j>-1 and not temp[idx-j][i-j]:
                            temp[idx-j][i-j]='.'
                        if idx+j<n and i+j<n and not temp[idx+j][i+j]:
                            temp[idx+j][i+j]='.'
                        if idx-j>-1 and i+j<n and not temp[idx-j][i+j]:
                            temp[idx-j][i+j]='.'
                        if idx+j<n and i-j>-1 and not temp[idx+j][i-j]:
                            temp[idx+j][i-j]='.'
                    bt(idx+1)
                    temp=snapshot
            return
        bt(0)
        return ans
            


                        
            
            
