class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=dict()
        for n in nums:
            if n in d.keys():
                return True
            else:
                d[n]=0 
        return False