class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp practice 1
        #d[i]=max(skip->robbed till last house is the same ans, take+dp[further-back])
        #base case for the first two houses would be the max of the first two houses
        #for each step all i need prev two steps values + last steps take
        if len(nums)==1:
            return nums[0]
        u=nums[0]
        v=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=max(v,u+nums[i])
            u,v=v,temp
        return v

        