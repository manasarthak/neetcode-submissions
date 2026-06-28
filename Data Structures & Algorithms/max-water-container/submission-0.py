class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        cand=0
        while cand<len(heights):
            nxt=-1
            for i in range(cand+1,len(heights)):
                res=max(res,min(heights[cand],heights[i])*(i-cand))
            for j in range(cand+1,len(heights)):
                if heights[j]>heights[cand]:
                    nxt=j
                    break
            if nxt==-1:
                break
            cand=nxt
        return res


        