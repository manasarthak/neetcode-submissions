class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        r=len(nums)-1
        while r>1:
            if r < len(nums) - 1 and nums[r] == nums[r+1]:
                r -= 1
                continue
            lo,hi=0,r-1
            while lo<hi:
                temp=nums[lo]+nums[hi]
                if temp==-nums[r]:
                    res.append([nums[lo],nums[hi],nums[r]])
                    while lo < hi and nums[lo]==nums[lo+1]:
                        lo+=1
                    lo += 1
                elif temp<-nums[r]:
                    lo+=1
                else:
                    hi-=1
            r-=1
        return res