class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        left_less=[-1]*len(heights)
        for i in range(len(heights)):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if stack:
                left_less[i]=stack[-1][1]
            stack.append([heights[i],i])
        stack=[]
        right_less=[len(heights)]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and stack[-1][0]>=heights[i]:
                stack.pop()
            if stack:
                right_less[i]=stack[-1][1]
            stack.append([heights[i],i])
        ans=0

        for i in range(len(heights)):
            ans=max(ans,heights[i]*(right_less[i]-1-left_less[i]))
        return ans
            

            
            




        