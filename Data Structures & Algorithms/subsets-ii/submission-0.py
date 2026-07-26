class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()
        def bt(start):
            if start==len(nums):
                ans.append(temp[:])
                return
            temp.append(nums[start])
            bt(start+1)
            temp.pop()
            while start<len(nums)-1 and nums[start]==nums[start+1]:
                start+=1
            start+=1
            bt(start)
            return
        bt(0)
        return ans
        