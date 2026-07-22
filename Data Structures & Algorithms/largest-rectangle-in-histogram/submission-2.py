class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        left_can=[0]
        right_can=[n-1]
        for i in range(0,n-1):
            if heights[i]<heights[i+1]:
                left_can.append(i+1)
            elif heights[i]>heights[i+1]:
                right_can.append(i)
        print(left_can)
        print(right_can)
        ans=-1
        for i in left_can:
            for j in right_can:
                if i<=j:
                    num=min(heights[i:j+1])
                    ans=max(ans,num*(j-i+1))
        for num in heights:
            ans=max(ans,num)
        return ans


        
        