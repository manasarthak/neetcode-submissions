import math
class Solution:
    def climbStairs(self, n: int) -> int:
        max_2=n//2
        ans=1
        for i in range(1,max_2+1):
            ans+=math.factorial(n-i)/(math.factorial(i)*math.factorial(n-2*i))
        return int(ans)