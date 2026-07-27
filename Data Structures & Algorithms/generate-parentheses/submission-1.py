class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op=['(']*n
        ans=[]
        temp=['(']
        def bt(cnt_op,cnt_cl):
            if cnt_op==n:
                start=len(temp)
                for j in range(start,2*n):
                    temp.append(')')
                ans.append(''.join(temp[:]))
                for j in range(start,2*n):
                    temp.pop()
                return
            if cnt_op>cnt_cl:
                temp.append(')')
                bt(cnt_op,cnt_cl+1)
                temp.pop()
            if cnt_op<n:
                temp.append('(')
                bt(cnt_op+1,cnt_cl)
                temp.pop()
            return
        bt(1,0)
        return ans
                
            
            

        