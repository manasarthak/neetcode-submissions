class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi=lo=nums[0]
        if len(nums)==1:
            return nums[0]
        ans=float('-inf')
        for i in range(1,len(nums)):
            #at each number we have three choices: start from it for the ans, or multiply it by the max an dmin we have seen before until the last element; min because negative would lead to min that we would want to consider in case it flips
            new=nums[i]
            
            hi,lo=max(new,hi*new,lo*new),min(new,lo*new,hi*new)
            ans=max(ans,hi)
            #after we include this new number as seen we consider only subarrays which end at this number hence why we keep a ans as global tracker for every subarray that eneds t i and we take the max at each one of them..
        return ans
        