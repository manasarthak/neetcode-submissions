class Solution:
    def rob(self, nums: List[int]) -> int:
        #first house and last house can never be together even thouigh they dont follow the 
        #pattern we wrote upto house i max rob amount= max_amount_(i-1)(we dont select current) or max_amount_(i-2)+nums[i]
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        u,v=nums[0],max(nums[0],nums[1])
        for i in range(2,n-1):
            temp=max(u+nums[i],v)
            u,v=v,temp
        x,y=nums[1],max(nums[1],nums[2])
        for i in range(3,n):
            temp=max(x+nums[i],y)
            x,y=y,temp
        return max(v,y)
        