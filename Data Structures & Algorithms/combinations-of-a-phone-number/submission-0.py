class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans=[]
        temp=[]
        mp={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        def bt(idx):
            if idx==len(digits):
                ans.append(''.join(temp))
                return
            for i in range(len(mp[digits[idx]])):
                temp.append(mp[digits[idx]][i])
                bt(idx+1)
                temp.pop()
            return
        bt(0)
        return ans
            

        