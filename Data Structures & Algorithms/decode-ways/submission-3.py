class Solution:
    def numDecodings(self, s: str) -> int:
        #first we write the recursive solution(decision tree)
        dp=[0]*(len(s)+1)
        dp[len(s)]=1
        def dfs(i):
            if dp[i]!=0:
                return dp[i] #remember counting problems base case is 1
            if s[i]=='0':
                return 0 #cannot take 0 as the starting of any sequence that we can decode
            res=dfs(i+1)
            if i<len(s)-1:
                if (s[i]=='1' or (s[i]=='2' and s[i+1]<'7')):
                    res+=dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)