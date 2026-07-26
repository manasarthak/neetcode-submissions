class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        temp=[]
        candidates.sort()
        def dfs(start,running_sum):
            if running_sum>=target:
                if running_sum==target:
                    ans.append(temp[:])
                return
            i=start
            while i<len(candidates):
                temp.append(candidates[i])
                dfs(i+1,running_sum+candidates[i])
                temp.pop()
                j=i+1
                while j<len(candidates) and candidates[i]==candidates[j]:
                    j+=1
                i=j
            return
        dfs(0,0)
        return ans
        