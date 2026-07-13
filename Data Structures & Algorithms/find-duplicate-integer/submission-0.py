class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp={}
        for num in nums:
            if num in mp.keys():
                return num
            else:
                mp[num]=1
        
            

        
        
        