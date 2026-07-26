class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        def dfs(choose_from):
            if len(temp)==len(nums):
                ans.append(temp[:])
                return
            for i in range(len(choose_from)):
                temp.append(choose_from[i])
                dfs(choose_from[:i]+choose_from[i+1:])
                temp.pop()
            return
        dfs(nums)
        return ans
        
        