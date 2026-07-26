class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def recurse(temp,idx):
            if idx==len(nums):
                ans.append(temp)
                return
            recurse(temp+[nums[idx]],idx+1)
            recurse(temp,idx+1)
            return
        recurse([],0)
        return ans

        