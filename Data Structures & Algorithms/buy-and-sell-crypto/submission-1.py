class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof=0
        min_l=prices[0]
        for i in range(1,len(prices)):
            prof=max(prof,prices[i]-min_l)
            min_l=min(min_l,prices[i])
        return prof
        