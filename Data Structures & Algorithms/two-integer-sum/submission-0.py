class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], []) + [i]
        i,j=-1,-1
        for n in nums:
            if (target-n) in d.keys():
                if n!=target-n:
                    i,j=d[n][0],d[target-n][0]
                elif len(d[n]) > 1:
                    i,j=d[n][0],d[n][1]
                else:
                    continue
                break
        if i<j:
            return [i,j]

        else:
            return [j,i]
