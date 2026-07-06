import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi=1,max(piles)
        ans=0
        while lo<=hi:
            mid=(lo+hi)//2
            hrs=0
            for i in range(len(piles)):
                hrs+=math.ceil(piles[i]/mid)
            if hrs>h:
                lo=mid+1
            else:
                ans=mid
                hi=mid-1
        return ans
                



        