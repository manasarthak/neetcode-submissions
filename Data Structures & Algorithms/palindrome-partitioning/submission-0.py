class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(i,j):
            if s[i:j]==s[i:j][::-1]:
                return True
            else:
                return False
        ans=[]
        temp=[]
        def bt(i):
            if i==len(s):
                ans.append(temp[:])
                return
            for j in range(i+1,len(s)+1):
                if palindrome(i,j):
                    temp.append(s[i:j])
                    bt(j)
                    temp.pop()
            return
        bt(0)
        return ans


            
            

        