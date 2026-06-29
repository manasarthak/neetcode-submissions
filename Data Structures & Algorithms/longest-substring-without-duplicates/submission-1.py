class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        mp={s[0]:0}
        lf=0
        ans=1
        for i in range(1,len(s)):
            if s[i] in mp.keys():
                if lf<=mp[s[i]]:
                    lf=mp[s[i]]+1
            mp[s[i]]=i
            ans=max(ans,i-lf+1)
        return ans
                


        