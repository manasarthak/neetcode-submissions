class Solution:
    def rob(self, nums: List[int]) -> int:
        #easy distialltion here is we break this into max of house robber 1 problem 1-n-1 and 2-n houses 
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])

        u1,v1=nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            temp=max(u1+nums[i],v1)
            u1,v1=v1,temp
        u2,v2=nums[1],max(nums[2],nums[1])
        for i in range(3,len(nums)):
            temp=max(u2+nums[i],v2)
            u2,v2=v2,temp
        return max(v1,v2)
        
        