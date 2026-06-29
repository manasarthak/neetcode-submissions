class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_ch,lo,hi=0,0,0
        ans=1
        mp={}
        while lo<=hi and hi<len(s):
            mp[s[hi]]=mp.get(s[hi],0)+1
            max_ch=max(max_ch,mp[s[hi]])
            if max_ch+k<hi-lo+1:         
                mp[s[lo]]-=1
                lo+=1
            else:
                ans=max(ans,hi-lo+1)
            hi+=1
        return ans

        

        