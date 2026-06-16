class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if  diff not in d:
                d[nums[i]] = i
            else: 
                return [d[diff], i]
        
        return []