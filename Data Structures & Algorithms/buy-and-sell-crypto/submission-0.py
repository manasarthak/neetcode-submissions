class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_r=[prices[-1]]*len(prices)
        for i in range(len(prices)-2,-1,-1):
            max_r[i]=max(max_r[i+1],prices[i+1])
        prof=0
        for i in range(len(prices)):
            prof=max(prof,max_r[i]-prices[i])
        return prof
        