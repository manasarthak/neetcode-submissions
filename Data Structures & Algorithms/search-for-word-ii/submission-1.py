import json
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root={}
        visited=[[False for i in range (len(board[0]))] for i in range(len(board))]
        def dfs(i,j,temp,depth):
            if i<0 or j<0 or i>=len(board) or j >=len(board[0]) or visited[i][j] or depth>10:
                return
            idx=ord(board[i][j])-ord('a')
            visited[i][j]=True
            if idx not in temp.keys():
                temp[idx]={}
            dfs(i+1,j,temp[idx],depth+1)
            dfs(i-1,j,temp[idx],depth+1)
            dfs(i,j+1,temp[idx],depth+1)
            dfs(i,j-1,temp[idx],depth+1)
            visited[i][j]=False
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root,0)
        ans=[]
        #print(json.dumps(root, indent=4))
        for word in words:
            temp=root
            for i,ch in enumerate(word):
                idx=ord(ch)-ord('a')
                #print("check for",ch)
                if idx not in temp.keys():
                    break
                #print("pass for",ch)
                temp=temp[idx]
                if i==len(word)-1:
                    ans.append(word)
        return ans

        