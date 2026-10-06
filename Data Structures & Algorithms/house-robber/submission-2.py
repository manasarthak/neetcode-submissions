class Solution:
    def rob(self, nums: List[int]) -> int:
        ans=0
        df=[0]*len(nums)
        df[0]=nums[0]
        for i in range(1,len(nums)):
            if i>1:
                df[i]=max(df[i-1],df[i-2]+nums[i])
            else:
                df[i]=max(df[i-1],nums[i])
        return df[-1]

        