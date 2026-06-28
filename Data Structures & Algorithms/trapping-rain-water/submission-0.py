class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[height[0]]*n
        max_right=[height[-1]]*n
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i-1])
            max_right[n-i-1]=max(max_right[n-i],height[n-i])
        res=0
        for i in range(0,n):
            cand=min(max_left[i],max_right[i])
            if cand<=height[i]:
                continue
            else:
                res+=cand-height[i]
        return res


        