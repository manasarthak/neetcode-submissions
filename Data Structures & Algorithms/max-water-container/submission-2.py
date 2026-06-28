class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        cand=0
        while cand<len(heights):
            nxt=-1
            for i in range(cand+1,len(heights)):
                res=max(res,min(heights[cand],heights[i])*(i-cand))
                if heights[i]>heights[cand] and nxt==-1:
                    nxt=i
            if nxt==-1:
                break
            cand=nxt
        return res


        