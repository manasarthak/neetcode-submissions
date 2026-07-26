class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        temp=[]
        ans=[]
        def dfs(start,running_sum):
            if running_sum>=target:
                if running_sum==target:
                    ans.append(temp[:])
                return
            for i in range(start,len(nums)):
                temp.append(nums[i])
                dfs(i,running_sum+nums[i])
                temp.pop()
            return
        dfs(0,0)
        return ans
            
            

        