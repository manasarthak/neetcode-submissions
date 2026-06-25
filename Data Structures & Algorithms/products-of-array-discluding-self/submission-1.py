class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[nums[0]]*len(nums)
        right=[nums[-1]]*len(nums)
        for i in range(1,len(nums)):
            left[i]=left[i-1]*nums[i]
            right[len(nums)-i-1]=right[len(nums)-i]*nums[len(nums)-i-1]
        res=[right[1]]*len(nums)
        res[-1]=left[len(nums)-2]
        for i in range(1,len(nums)-1):
            res[i]=left[i-1]*right[i+1]
        return res
    

